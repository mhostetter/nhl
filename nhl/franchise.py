"""
Module containing NHL franchise objects
"""
from dataclasses import dataclass, field, InitVar

from .flyweight import Flyweight

@dataclass(frozen=True)
class Franchise(Flyweight):
    """
    NHL franchise object.

    This is the detailed docstring.
    """
    __slots__ = ["id", "name"]
    _instances = {}

    id: int
    """int: The NHL statsapi universal franchise ID"""

    name: str
    """str: Franchise name"""

    def _key(cls, id, *args, **kwargs):
        return id
