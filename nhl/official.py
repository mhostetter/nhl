"""
Module containing NHL official objects
"""
from dataclasses import dataclass

from .flyweight import Flyweight

@dataclass(frozen=True)
class Official(Flyweight):
    """
    NHL official object.

    This is the detailed docstring.
    """

    __slots__ = ["id", "name"]
    _instances = {}

    id: int
    """int: The NHL statsapi universal official ID"""

    name: str
    """str: Official's full name"""

    @classmethod
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
            nhl.Official or None: Previously constructed flyweight object with given
            key or `None` if key not found
        """
        return super().from_key(id)

    def __repr__(self):
        return "<nhl.Official: {}, ID {}>".format(self.name, self.id)

    @property
    def first_name(self):
        """str: Official's first name"""
        return self.name.split(" ", 1)[0]

    @property
    def last_name(self):
        """str: Official's last name"""
        return self.name.split(" ", 1)[1]
