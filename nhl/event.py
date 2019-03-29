"""
Module containing NHL event objects
"""
from dataclasses import dataclass

from .flyweight import Flyweight
from .gametime import Gametime
from .list import List
from .location import Location
from .player import Player
from .team import Team
from .venue import Venue

@dataclass(frozen=True)
class Event(Flyweight):
    """
    NHL event object.

    This is the detailed docstring.
    """
    __slots__ = ["game_id", "id", "type", "subtype", "time", "location", "team", "by", "on"]
    _instances = {}

    game_id: int
    id: int
    type: str
    subtype: str
    time: Gametime
    location: Location
    team: Team
    by: List
    on: Player

    def _key(cls, game_id, id, *args, **kwargs):
        return (game_id, id)

    @classmethod
    def has_key(cls, game_id, id):
        """
        Check whether flyweight object with specified key has already been created.

        Returns:
            bool: True if already created, False if not
        """
        return super().has_key(game_id, id)

    @classmethod
    def from_key(cls, game_id, id):
        """
        Return flyweight object with specified key, if it has already been created.

        Returns:
            nhl.Event or None: Previously constructed flyweight object with given
            key or `None` if key not found
        """
        return super().from_key(game_id, id)
