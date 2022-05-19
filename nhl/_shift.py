"""
A module with functions to fetch/parse and a class to contain an NHL shift.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from bs4 import BeautifulSoup

from . import _player
from ._api import fetch
from ._gametime import GameTime
from ._overrides import set_module


def parse(game_id: int, player_id: int, name: str, home_html: str, away_html: str) -> Optional[List[Shift]]:
    """
    Scrapes the HTML page . Returns `None` if the player is not found.
    """
    shifts_ = []
    found = False

    for html in [home_html, away_html]:
        tree = BeautifulSoup(html, features="html.parser")
        for row in tree.find_all("td",  "playerHeading + border"):
            if name not in row.get_text():
                continue
            found = True

            row = row.find_next("tr")
            while True:
                row = row.find_next("tr")
                cells = row.find_all("td")
                if len(cells) == 6:
                    shift_id = int(cells[0].get_text()) - 1
                    period = int(cells[1].get_text())
                    on_period_mmss = cells[2].get_text().split(" /")[0]
                    off_period_mmss = cells[3].get_text().split(" /")[0]
                    on = GameTime(period, convert_gametime(on_period_mmss))
                    off = GameTime(period, convert_gametime(off_period_mmss))
                    shift = Shift(game_id, player_id, shift_id, on, off)
                    shifts_.append(shift)
                else:
                    break

    if not found:
        return None

    return shifts_


def convert_gametime(period_time: str) -> int:
    """
    Converts a string of the form "mm:ss" to total seconds.
    """
    return 60*int(period_time.split(":")[0]) + int(period_time.split(":")[1])


@set_module("nhl.statsapi")
def shifts(game_id: int, player_id: int) -> List[Shift]:
    """
    Fetches all shifts of a player of a given game.

    Parameters
    ----------
    game_id
        The NHL statsapi game ID.
    player_id
        The NHL statsapi player ID.

    Returns
    -------
    :
        A list of :obj:`~nhl.Shift` objects.

    Raises
    ------
    ValueError
        If the player is not found in the game.
    """
    season_id = game_id // 1000000
    lower_game_id = game_id % 1000000
    home = fetch("{:04d}{:04d}/TH{:06d}.HTM".format(season_id, season_id + 1, lower_game_id), "htmlreports")  # pylint: disable=consider-using-f-string
    away = fetch("{:04d}{:04d}/TV{:06d}.HTM".format(season_id, season_id + 1, lower_game_id), "htmlreports")  # pylint: disable=consider-using-f-string

    player = _player.player(player_id)
    name = player.last_name.upper() + ", " + player.first_name.upper()

    shifts_ = parse(game_id, player_id, name, home.text, away.text)

    if shifts_ is None:
        raise ValueError(f"Player \"{name}\" not found in home team shift report {home.url} or away shift report {away.url}.")

    return shifts_


@set_module("nhl.statsapi")
@dataclass(frozen=True)
class Shift:
    """
    NHL shift object.
    """

    game_id: int
    """NHL statsapi unique game ID"""

    player_id: int
    """NHL statsapi unique player ID"""

    shift_id: int
    """Shift number for specified game"""

    on: GameTime
    """Shift start game time"""

    off: GameTime
    """Shift end game time"""

    length: int = field(init=False)
    """Shift length in seconds"""

    def __post_init__(self):
        object.__setattr__(self, "length", self.off.sec - self.on.sec)

    def __repr__(self):
        # pylint: disable=consider-using-f-string
        return "<nhl.Shift: {} {:02d}:{:02d} to {:02d}:{:02d}, {:>3d} s, ID {}.{}.{}>".format(self.on.period_str, *self.on.period_min_sec, *self.off.period_min_sec, self.length, self.game_id, self.player_id, self.shift_id)
