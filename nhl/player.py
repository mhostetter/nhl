"""
Module containing NHL player objects
"""

from dataclasses import dataclass, field, InitVar
import datetime

@dataclass(frozen=True)
class Player:
    """
    NHL player object.

    This is the detailed docstring.
    """
    id: int
    """int: The NHL statsapi universal player ID"""

    name: str = None
    """str: Player's full name"""

    number: int = None
    """int: Player's primary number"""

    position: str = None
    """str: Player's primary position ("LW", "C", "RW", "D", "G")"""

    height: int = None
    """int: Player's height in total inches"""

    weight: int = None
    """int: Player's weight in lbs"""

    shoots_catches: str = None
    """str: Indication of whether the player shoots (skater)/catches (goalie) "L" or "R" """

    birth_date_str: InitVar[str] = None
    birth_date: datetime.date = field(init=False)
    """:class:`datetime.date`: Player's birth date"""

    birth_city: str = None
    """str: Player's birth city"""

    birth_country: str = None
    """str: Player's birth country"""

    def __post_init__(self, birth_date_str):
        if birth_date_str:
            year = int(birth_date_str.split("-")[0])
            month = int(birth_date_str.split("-")[1])
            day = int(birth_date_str.split("-")[2])
            object.__setattr__(self, "birth_date", datetime.date(year, month, day))
        else:
            object.__setattr__(self, "birth_date", None)

    @property
    def first_name(self):
        """str: Player's first name"""
        return self.name.split(" ", 1)[0]

    @property
    def last_name(self):
        """str: Player's last name"""
        return self.name.split(" ", 1)[1]

    @property
    def height_ft(self):
        """int: Height in feet (:py:attr:`height` // 12)"""
        return self.height // 12 if self.height else None

    @property
    def height_in(self):
        """int: Height in inches (:py:attr:`height` % 12)"""
        return self.height % 12 if self.height else None
