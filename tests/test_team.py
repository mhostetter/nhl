"""
A pytest module to test the `nhl.Team` class.
"""
import dataclasses
import pytest

import nhl


def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        nhl.Team()


def test_frozen(mock_teams):
    team = nhl.statsapi.team(15)
    with pytest.raises(dataclasses.FrozenInstanceError):
        team.id = 2


# def test_flyweight(mock_teams):
#     team_1 = nhl.statsapi.team(15)
#     team_2 = nhl.statsapi.team(15)
#     assert team_1 is team_2
#     assert team_1 == team_2


def test_fetch_and_parse(mock_teams):
    team = nhl.statsapi.team(15)
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


def test_fetch_and_parse_all(mock_teams):
    teams = nhl.statsapi.teams()
    assert [team.id for team in teams] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 52, 53, 54, 55]
    assert [team.name for team in teams] == ["Devils", "Islanders", "Rangers", "Flyers", "Penguins", "Bruins", "Sabres", "Canadiens", "Senators", "Maple Leafs", "Hurricanes", "Panthers", "Lightning", "Capitals", "Blackhawks", "Red Wings", "Predators", "Blues", "Flames", "Avalanche", "Oilers", "Canucks", "Ducks", "Stars", "Kings", "Sharks", "Blue Jackets", "Wild", "Jets", "Coyotes", "Golden Knights", "Kraken"]
