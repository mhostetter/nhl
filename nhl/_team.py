"""
A module with functions to fetch/parse and a class to contain an NHL team.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict

from . import _conference, _division, _franchise
from ._api import fetch
from ._overrides import set_module


def parse(json: Dict) -> Team:
    """
    Parses the JSON response from the NHL statsapi.
    """
    id = json["id"]
    # if Team.has_key(id):
    #     return Team.from_key(id)

    location = json["locationName"]
    name = json["teamName"]
    abbreviation = json["abbreviation"]
    first_year = int(json["firstYearOfPlay"])
    division = _division.parse(json["division"])
    conference = _conference.parse(json["conference"])
    franchise = _franchise.parse(json["franchise"])

    return Team(id, location, name, abbreviation, first_year, division, conference, franchise)


@set_module("nhl.statsapi")
def team(id: int) -> Team:
    """
    Fetches a single team by its ID.

    Parameters
    ----------
    id
        The NHL statsapi team ID.

    Returns
    -------
    :
        A :obj:`~nhl.Team` object.
    """
    json = fetch(f"teams/{id}").json()
    return parse(json["teams"][0])


@set_module("nhl.statsapi")
def teams() -> List[Team]:
    """
    Fetches all teams.

    Returns
    -------
    :
        A list of :obj:`~nhl.Team` objects.
    """
    json = fetch("teams/").json()
    return list(parse(item) for item in json["teams"])


@set_module("nhl.statsapi")
@dataclass(frozen=True)
class Team:
    """
    NHL team object.
    """

    id: int
    """The NHL statsapi universal team ID"""

    location: str
    """Team's location"""

    name: str
    """Team's name"""

    abbreviation: str
    """Team's name abbreviated"""

    first_year: int
    """First year of play"""

    division: _division.Division
    """The NHL division the team is in"""

    conference: _conference.Conference
    """The NHL conference the team is in"""

    franchise: _franchise.Franchise
    """The NHL franchise the team belongs to"""

    def __repr__(self):
        return f"<nhl.Team: {self.name}, {self.division.name} Division, {self.conference.name} Conference, ID {self.id}>"

    @property
    def full_name(self) -> str:
        """Team's full name"""
        return f"{self.location} {self.name}"
