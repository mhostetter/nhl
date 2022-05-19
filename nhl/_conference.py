"""
A module with functions to fetch/parse and a class to contain an NHL conference.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict

from ._api import fetch
from ._overrides import set_module


def parse(json: Dict) -> Conference:
    """
    Parses the JSON response from the NHL statsapi.
    """
    id = json["id"]
    # if Conference.has_key(id):
    #     return Conference.from_key(id)

    name = json["name"]
    # NOTE: `nameShort` and `abbreviation` keys are not guaranteed. It depends on
    # which json object is returned.
    name_short = json.get("shortName", name[0:-3])
    abbreviation = json.get("abbreviation", name[0])

    return Conference(id, name, name_short, abbreviation)


@set_module("nhl.statsapi")
def conference(id: int) -> Conference:
    """
    Fetches a single conference by its ID.

    Parameters
    ----------
    id
        The NHL statsapi conference ID.

    Returns
    -------
    :
        A :obj:`~nhl.Conference` object.
    """
    json = fetch(f"conferences/{id}").json()
    return parse(json["conferences"][0])


@set_module("nhl.statsapi")
def conferences() -> List[Conference]:
    """
    Fetches all conferences.

    Returns
    -------
    :
        A list of :obj:`~nhl.Conference` objects.
    """
    json = fetch("conferences/").json()
    return list(parse(item) for item in json["conferences"])


@set_module("nhl")
@dataclass(frozen=True)
class Conference:
    """
    NHL conference object.
    """

    id: int
    """The NHL statsapi universal conference ID"""

    name: str
    """Conference name"""

    name_short: str
    """Conference name shortened"""

    abbreviation: str
    """Conference abbreviation"""

    def __repr__(self):
        return f"<nhl.Conference: {self.name}, ID {self.id}>"
