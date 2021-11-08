"""
Module containing NHL conference objects
"""
from dataclasses import dataclass

from .flyweight import Flyweight


@dataclass(frozen=True)
class Conference(Flyweight):
    """
    NHL conference object.

    This is the detailed docstring.
    """

    __slots__ = ["id", "name", "name_short", "abbreviation"]
    _instances = {}

    id: int
    """int: The NHL statsapi universal conference ID"""

    name: str
    """str: Conference name"""

    name_short: str
    """str: Conference name shortened"""

    abbreviation: str
    """str: Conference abbreviation"""

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
        return f"<nhl.Conference: {self.name}, ID {self.id}>"
