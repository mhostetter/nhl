from dataclasses import dataclass, field, InitVar
import datetime

@dataclass(frozen=True)
class Player:
    """NHL player object.

    This is the detailed docstring.

    Attributes:    
        id (int): player's NHL statsapi universal ID
        name (int): player's full name
        birth_date (datetime.date): player's date of birth
        birth_city (str): player's birth city
        birth_country (str): player's birth country

        first_name (str): player's first name
        last_name (str): player's last name
        height_ft (int): player's height in feet
        height_in (int): player's height in inches
    """
    id: int
    name: str = ""
    number: int = None
    position: str = None
    height: int = None
    weight: int = None
    shoots_catches: str = None
    birth_date_str: InitVar[str] = None
    birth_date: datetime.date = field(init=False)
    birth_city: str = ""
    birth_country: str = ""

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
        return self.name.split(" ", 1)[0]

    @property
    def last_name(self):
        return self.name.split(" ", 1)[1]

    @property
    def height_ft(self):
        return self.height // 12 if self.height else None

    @property
    def height_in(self):
        return self.height % 12 if self.height else None
