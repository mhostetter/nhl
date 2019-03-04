import dataclasses
import datetime
import pytest

import nhl

def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        team = nhl.Team()

def make_team():
    return nhl.statsapi.fetch_team(15)

def test_frozen():
    team = make_team()
    with pytest.raises(dataclasses.FrozenInstanceError):
        team.id = 2

def test_flyweight():
    team_1 = make_team()
    team_2 = make_team()
    assert team_1 is team_2
    assert team_1 == team_2

def test_values():
    team = make_team()
    assert team.id == 15
    assert team.location == "Washington"
    assert team.name == "Capitals"
    assert team.abbreviation == "WSH"
    assert team.first_year == 1974
    assert team.division.id == 18
    assert team.division.name == "Metropolitan"
    assert team.division.name_short == "Metro"
    assert team.division.abbreviation == "M"
    assert team.conference.id == 6
    assert team.conference.name == "Eastern"
    assert team.conference.name_short == "East"
    assert team.conference.abbreviation == "E"
    assert team.franchise.id == 24
    assert team.franchise.name == "Capitals"
