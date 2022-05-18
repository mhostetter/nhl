"""
A module with functions to fetch/parse and a class to contain an NHL venue.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict

from ._api import fetch
from ._overrides import set_module


def parse(json: Dict) -> Venue:
    """
    Parses the JSON response from the NHL statsapi.
    """
    id = json["id"]
    # if Venue.has_key(id):
    #     return Venue.from_key(id)

    name = json["name"]

    return Venue(id, name)


@set_module("nhl.statsapi")
def venue(id: int) -> Venue:
    """
    Fetches a single venue by its ID.

    Parameters
    ----------
    id
        The NHL statsapi venue ID.

    Returns
    -------
    :
        A :obj:`~nhl.Venue` object.
    """
    json = fetch(f"venues/{id}")
    return parse(json["venues"][0])


@set_module("nhl.statsapi")
def venues() -> List[Venue]:
    """
    Fetches all venues.

    Returns
    -------
    :
        A list of :obj:`~nhl.Venue` objects.
    """
    json = fetch("venues/")
    return list(parse(item) for item in json["venues"])


@set_module("nhl")
@dataclass(frozen=True)
class Venue:
    """
    NHL venue object.
    """

    id: int
    """The NHL statsapi universal venue ID"""

    name: str
    """Venue name"""

    def __repr__(self):
        return f"<nhl.Venue: {self.name}, ID {self.id}>"
