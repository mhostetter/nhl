"""
Module containing NHL team objects
"""
from dataclasses import dataclass
import datetime

from .conference import Conference
from .division import Division
from .flyweight import Flyweight
from .franchise import Franchise

@dataclass(frozen=True)
class Team(Flyweight):
    """
    NHL team object.

    This is the detailed docstring.
    """

    __slots__ = ["id", "location", "name", "abbreviation", "first_year", "division", 
        "conference", "franchise"]
    _instances = {}

    id: int
    """int: The NHL statsapi universal team ID"""

    location: str
    """str: Team's location"""

    name: str
    """str: Team's name"""

    abbreviation: str
    """int: Team's name abbreviated"""

    first_year: int
    """int: First year of play"""

    division: Division
    """Division: """

    conference: Conference
    """Conference: """

    franchise: Franchise
    """Franchise: """

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
            nhl.Team or None: Previously constructed flyweight object with given
            key or `None` if key not found
        """
        return super().from_key(id)

    def __repr__(self):
        return "<nhl.Team: {}, {} Division, {} Conference, ID {}>".format(self.name, self.division.name, self.conference.name, self.id)

    @property
    def full_name(self):
        """str: Team's full name"""
        return "{} {}".format(self.location, self.name)
