"""
Module containing NHL game objects
"""
from dataclasses import dataclass

from .flyweight import Flyweight
from .list import List
from .team import Team
from .venue import Venue

@dataclass(frozen=True)
class Game(Flyweight):
    """
    NHL game object.

    This is the detailed docstring.
    """
    __slots__ = ["id", "home", "away", "venue", "players", "events"]
    _instances = {}

    id: int
    """int: The NHL statsapi universal game ID"""

    home: Team
    """Team: Game home"""

    away: Team
    """Team: Game away"""

    venue: Venue
    """Venue: """

    players: List
    """List: """

    events: List
    """List: """

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
