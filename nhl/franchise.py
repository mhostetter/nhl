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
            nhl.Franchise or None: Previously constructed flyweight object with given
            key or `None` if key not found
        """
        return super().from_key(id)
