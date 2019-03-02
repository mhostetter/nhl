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
    _instances = {}

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
            nhl.Venue or None: Previously constructed flyweight object with given
            key or `None` if key not found
        """
        return super().from_key(id)
