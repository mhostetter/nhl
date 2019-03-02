"""
Module containing NHL conference objects
"""
from dataclasses import dataclass, field, InitVar

from .flyweight import Flyweight

@dataclass(frozen=True)
class Conference(Flyweight):
    """
    NHL conference object.

    This is the detailed docstring.
    """
    __slots__ = ["id", "name"]
    _instances = {}

    id: int
    """int: The NHL statsapi universal conference ID"""

    name: str
    """str: Conference name"""

    def _key(cls, id, *args, **kwargs):
        return id
