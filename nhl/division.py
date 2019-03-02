"""
Module containing NHL division objects
"""
from dataclasses import dataclass, field, InitVar

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

    def _key(cls, id, *args, **kwargs):
        return id
