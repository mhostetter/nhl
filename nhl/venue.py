"""
Module containing NHL venue objects
"""
from dataclasses import dataclass

from .flyweight import Flyweight


@dataclass(frozen=True)
class Venue(Flyweight):
    """
    NHL venue object.

    This is the detailed docstring.
    """

    __slots__ = ["id", "name"]
    _instances = {}

    id: int
    """int: The NHL statsapi universal venue ID"""

    name: str
    """str: Venue name"""

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
        return "<nhl.Venue: {}, ID {}>".format(self.name, self.id)
