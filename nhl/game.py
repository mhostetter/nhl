"""
Module containing NHL game objects
"""
from dataclasses import dataclass

from .flyweight import Flyweight
from .list import List
from .gameinfo import GameInfo
from .team import Team
from .venue import Venue

@dataclass(frozen=True)
class Game(Flyweight):
    """
    NHL game object.

    This is the detailed docstring.
    """

    __slots__ = ["info", "home", "away", "players", "events"]
    _instances = {}

    info: GameInfo
    """GameInfo: Game info"""

    home: Team
    """Team: Game home"""

    away: Team
    """Team: Game away"""

    players: List
    """List: """

    events: List
    """List: """

    @classmethod
    def _key(cls, info, *args, **kwargs):
        return info.id

    @classmethod
    def has_key(cls, id):
        return super().has_key(id)

    @classmethod
    def from_key(cls, id):
        return super().from_key(id)

    def __repr__(self):
        return "<nhl.Game: {}, {} ({}) at ({}) {}, {}, ID {}>".format(self.info.description, self.away.abbreviation, self.info.score[1], self.info.score[0], self.home.abbreviation, self.info.date, self.info.id)
        # return "<nhl.Game: {} at {}, ID {}>".format(self.away.abbreviation, self.home.abbreviation, self.id)

    @property
    def skaters(self):
        return self.players.filter("player.position", "G", "!=")

    @property
    def forwards(self):
        return self.players.filter("player.position", ["LW", "C", "RW"], "in")

    @property
    def defensemen(self):
        return self.players.filter("player.position", "D")

    @property
    def goalies(self):
        return self.players.filter("player.position", "G")
