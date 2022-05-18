"""
A module with functions to fetch/parse and a class to contain an NHL official.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from ._overrides import set_module


def parse(json: Dict) -> Official:
    """
    Parses the JSON response from the NHL statsapi.
    """
    id = json["id"]
    # if Official.has_key(id):
    #     return Official.from_key(id)

    name = json["fullName"]

    return Official(id, name)


@set_module("nhl")
@dataclass(frozen=True)
class Official:
    """
    NHL official object.
    """

    id: int
    """The NHL statsapi universal official ID"""

    name: str
    """Official's full name"""

    def __repr__(self):
        return f"<nhl.Official: {self.name}, ID {self.id}>"

    @property
    def first_name(self) -> str:
        """Official's first name"""
        return self.name.split(" ", 1)[0]

    @property
    def last_name(self) -> str:
        """Official's last name"""
        return self.name.split(" ", 1)[1]
