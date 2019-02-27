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

    id: int
    """int: The NHL statsapi universal franchise ID"""

    name: str
    """str: Franchise name"""

    def _key(cls, *args, **kwargs):
        return args[0]
