"""
Module containing NHL venue objects
"""
from dataclasses import dataclass, field, InitVar

from .flyweight import Flyweight

@dataclass(frozen=True)
class Venue(Flyweight):
    """
    NHL venue object.

    This is the detailed docstring.
    """
    __slots__ = ["id", "name", "city", "timezone", "timezone_offset"]

    id: int
    """int: The NHL statsapi universal venue ID"""

    name: str
    """str: Venue name"""

    city: str
    """int: Venue city"""

    timezone: str
    """str: Timezone of the venue"""

    timezone_offset: int
    """int: Timezone offset from UTC"""

    def _key(cls, *args, **kwargs):
        return args[0]
