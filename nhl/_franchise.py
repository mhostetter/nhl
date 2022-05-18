"""
A module with functions to fetch/parse and a class to contain an NHL franchise.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict

from ._api import fetch
from ._overrides import set_module


def parse(json: Dict) -> Franchise:
    """
    Parses the JSON response from the NHL statsapi.
    """
    id = json["franchiseId"]
    # if Franchise.has_key(id):
    #     return Franchise.from_key(id)

    name = json["teamName"]

    return Franchise(id, name)


@set_module("nhl.statsapi")
def franchise(id: int) -> Franchise:
    """
    Fetches a single franchise by its ID.

    Parameters
    ----------
    id
        The NHL statsapi franchise ID.

    Returns
    -------
    :
        A :obj:`~nhl.Franchise` object.
    """
    json = fetch(f"franchises/{id}")
    return parse(json["franchises"][0])


@set_module("nhl.statsapi")
def franchises() -> List[Franchise]:
    """
    Fetches all franchises.

    Returns
    -------
    :
        A list of :obj:`~nhl.Franchise` objects.
    """
    json = fetch("franchises/")
    return list(parse(item) for item in json["franchises"])


@set_module("nhl")
@dataclass(frozen=True)
class Franchise:
    """
    NHL franchise object.
    """

    id: int
    """The NHL statsapi universal franchise ID"""

    name: str
    """Franchise name"""

    def __repr__(self):
        return f"<nhl.Franchise: {self.name}, ID {self.id}>"
