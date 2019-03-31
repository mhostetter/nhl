"""
Module containing NHL location objects
"""
from dataclasses import dataclass
import math

from .flyweight import Flyweight

@dataclass(frozen=True)
class Location(Flyweight):
    """
    NHL location object.

    This is the detailed docstring.
    """

    __slots__ = ["x", "y"]
    _instances = {}

    x: int
    """int: Rink position in ft along x-axis (length) [-100, 100]"""

    y: int
    """int: Rink position in ft along y-axis (breadth) [-42, 42]"""

    @classmethod
    def _key(cls, x, y, *args, **kwargs):
        return (x, y)

    @classmethod
    def has_key(cls, x, y):
        """
        Check whether flyweight object with specified key has already been created.

        Returns:
            bool: True if already created, False if not
        """
        return super().has_key(x, y)

    @classmethod
    def from_key(cls, x, y):
        """
        Return flyweight object with specified key, if it has already been created.

        Returns:
            nhl.Location or None: Previously constructed flyweight object with given
            key or `None` if key not found
        """
        return super().from_key(x, y)

    def __repr__(self):
        return "<nhl.Location: {:3.0f}, {:3.0f}>".format(self.x, self.y)

    def distance(self, other):
        """
        Measure distance between current location and another on-ice location.

        Args:
            other (Location): location to measure distance from

        Returns:
            float: distance (ft)
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
