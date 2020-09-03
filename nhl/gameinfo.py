"""
Module containing NHL game info objects
"""
from dataclasses import dataclass
import datetime

from .list import List
from .gametime import Gametime
from .player import Player
from .team import Team
from .venue import Venue

@dataclass(frozen=True)
class GameInfo:
    """
    NHL game info.

    This is the detailed docstring.
    """

    __slots__ = ["id", "season_id", "type", "start", "end", "venue", "home_team", "away_team", "score", "end_type", "end_time", "referees", "linesmen"]
    _instances = {}

    id: int
    season_id: int
    type: str
    start: datetime.datetime
    end: datetime.datetime
    venue: Venue
    home_team: Team
    away_team: Team
    score: tuple
    end_type: str
    end_time: Gametime
    referees: List
    linesmen: List

    @classmethod
    def _key(cls, id, *args, **kwargs):
        return id

    @classmethod
    def has_key(cls, id):
        """
        Check whether flyweight object with specified key has already been created.

        Returns:
            bool: True if already created, False if not
        """
        return super().has_key(id)

    @classmethod
    def from_key(cls, id):
        """
        Return flyweight object with specified key, if it has already been created.

        Returns:
            nhl.Game or None: Previously constructed flyweight object with given
            key or `None` if key not found
        """
        return super().from_key(id)

    def __repr__(self):
        return "<nhl.GameInfo: {}, {} ({}) at ({}) {}, {}, ID {}>".format(self.description, self.away_team.abbreviation, self.score[1], self.score[0], self.home_team.abbreviation, self.date, self.id)

    @property
    def home_score(self):
        return self.score[0]

    @property
    def away_score(self):
        return self.score[1]

    @property
    def season(self):
        return self.id // 1000000

    @property
    def season_type(self):
        return (self.id // 10000) % 100

    @property
    def playoff_round(self):
        return (self.id // 100) % 100 if self.season_type == 3 else None

    @property
    def playoff_series(self):
        return (self.id // 10) % 10 if self.season_type == 3 else None

    @property
    def playoff_game(self):
        return self.id % 10 if self.season_type == 3 else None

    @property
    def description(self):
        if self.season_type == 1:
            s = "PS"
        elif self.season_type == 2:
            s = "RS"
        elif self.season_type == 3:
            if self.playoff_round in [1, 2]:
                r = "R{}".format(self.playoff_round)
            elif self.playoff_round == 3:
                r = "ECF" if self.playoff_series == 1 else " WCF"
            else:
                r = "SCF"
            s = "{} G{}".format(r, self.playoff_game)
        return "{:04d}-{:02d} {}".format(self.season, self.season % 100 + 1, s)

    @property
    def date(self):
        return self.start[0:10]
