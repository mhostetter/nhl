"""
A module with functions to fetch/parse and a class to contain an NHL player.
"""
from __future__ import annotations

import datetime
from dataclasses import dataclass
from typing import Tuple, List, Sequence, Dict

from ._api import fetch
from ._overrides import set_module


def parse(json: Dict) -> Player:
    """
    Parses the JSON response from the NHL statsapi.
    """
    id = json["id"]
    # if Player.has_key(id):
    #     return Player.from_key(id)

    name = json["fullName"]
    # NOTE: Occasionally this key is not provided
    _number = json.get("primaryNumber", None)
    number = int(_number) if _number else None
    position = json["primaryPosition"]["abbreviation"]
    height = convert_height(json["height"])
    weight = json["weight"]
    shoots_catches = json["shootsCatches"]
    birth_date = convert_date(json["birthDate"])
    birth_city = json["birthCity"]
    birth_country = json["birthCountry"]

    return Player(id, name, number, position, height, weight, shoots_catches, birth_date, birth_city, birth_country)


def convert_height(height_str: str) -> int:
    """
    Converts the height string from the NHL statsapi to inches. Ex: '6' 3"' -> 75 in.
    """
    feet = int(height_str.split("\' ")[0])
    inches = int(height_str.split("\' ")[1].split("\"")[0])
    return feet*12 + inches


def convert_date(date_str: str) -> datetime.date:
    """
    Converts the date string from the NHL statsapi to a date object. Ex: '1985-09-17' -> datetime.date(1985, 09, 17).
    """
    year = int(date_str.split("-")[0])
    month = int(date_str.split("-")[1])
    day = int(date_str.split("-")[2])
    return datetime.date(year, month, day)


@set_module("nhl.statsapi")
def player(id: int) -> Player:
    """
    Fetches a single player by its ID.

    Parameters
    ----------
    id
        The NHL statsapi player ID.

    Returns
    -------
    :
        A :obj:`~nhl.Player` object.
    """
    json = fetch(f"people/{id}").json()
    return parse(json["people"][0])


@set_module("nhl.statsapi")
def players(ids: Sequence[int]) -> List[Player]:
    """
    Fetches multiple players by their IDs.

    Returns
    -------
    :
        A list of :obj:`~nhl.Player` objects.
    """
    return list(player(id) for id in ids)


@set_module("nhl")
@dataclass(frozen=True)
class Player:
    """
    NHL player object.
    """

    id: int
    """The NHL statsapi universal player ID"""

    name: str
    """Player's full name"""

    number: int
    """Player's primary number"""

    position: str
    """Player's primary position ("LW", "C", "RW", "D", "G")"""

    height: int
    """Player's height in total inches"""

    weight: int
    """Player's weight in lbs"""

    shoots_catches: str
    """Indication of whether the player shoots (skater)/catches (goalie) "L" or "R" """

    birth_date: datetime.date
    """Player's birth date"""

    birth_city: str
    """Player's birth city"""

    birth_country: str
    """Player's birth country"""

    def __repr__(self):
        # pylint: disable=consider-using-f-string
        return "<nhl.Player: {:>2} {:<2} {:<20}, {}\'{:>2}\", {} lbs, ID {}>".format(self.number if self.number is not None else "", self.position, self.name, *self.height_ft_in, self.weight, self.id)

    @property
    def first_name(self) -> str:
        """Player's first name"""
        return self.name.split(" ", 1)[0]

    @property
    def last_name(self) -> str:
        """Player's last name"""
        return self.name.split(" ", 1)[1]

    @property
    def height_ft_in(self) -> Tuple[int, int]:
        """Height in feet and inches (:py:attr:`height` // 12, :py:attr:`height` % 12)"""
        if self.height:
            return (self.height // 12, self.height % 12)
        else:
            return (0, 0)

    @property
    def age(self) -> int:
        """Current age in years"""
        return (datetime.date.today() - self.birth_date).days // 365
