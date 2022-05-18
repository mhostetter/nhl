"""
A module with functions to fetch/parse and a class to contain an NHL division.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict

import requests

from ._overrides import set_module
from ._url import BASE


def parse(json: Dict) -> Division:
    """
    Parses the JSON response from the NHL statsapi.
    """
    id = json["id"]
    # if Division.has_key(id):
    #     return Division.from_key(id)

    name = json["name"]
    name_short = json["nameShort"]
    abbreviation = json["abbreviation"]

    return Division(id, name, name_short, abbreviation)


@set_module("nhl.statsapi")
def division(id: int) -> Division:
    """
    Fetches a single division by its ID.

    Parameters
    ----------
    id
        The NHL statsapi division ID.

    Returns
    -------
    :
        A :obj:`~nhl.Division` object.
    """
    json = requests.get(f"{BASE}/divisions/{id}").json()
    return parse(json["divisions"][0])


@set_module("nhl.statsapi")
def divisions() -> List[Division]:
    """
    Fetches all divisions.

    Returns
    -------
    :
        A list of :obj:`~nhl.Division` objects.
    """
    json = requests.get(f"{BASE}/divisions/").json()
    return list(parse(item) for item in json["divisions"])


@set_module("nhl")
@dataclass(frozen=True)
class Division:
    """
    NHL division object.
    """

    id: int
    """The NHL statsapi universal division ID"""

    name: str
    """Division name"""

    name_short: str
    """Division short name"""

    abbreviation: str
    """Division abbreviated name"""

    def __repr__(self):
        return f"<nhl.Division: {self.name} Division, ID {self.id}>"
