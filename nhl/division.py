"""
Module containing NHL division objects
"""
from dataclasses import dataclass

from .flyweight import Flyweight


@dataclass(frozen=True)
class Division(Flyweight):
    """
    NHL division object.

    This is the detailed docstring.
    """

    __slots__ = ["id", "name", "name_short", "abbreviation"]
    _instances = {}

    id: int
    """int: The NHL statsapi universal division ID"""

    name: str
    """str: Division name"""

    name_short: str
    """int: Division short name"""

    abbreviation: str
    """str: Division abbreviated name"""

    @classmethod
    def _key(cls, id, *args, **kwargs):
        return id

    @classmethod
    def has_key(cls, id):
        return super().has_key(id)

    @classmethod
    def from_key(cls, id):
        return super().from_key(id)

    def __repr__(self):
        return f"<nhl.Division: {self.name} Division, ID {self.id}>"
