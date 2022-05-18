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
    assert [team.location for team in teams] == ["New Jersey", "New York", "New York", "Philadelphia", "Pittsburgh", "Boston", "Buffalo", "Montréal", "Ottawa", "Toronto", "Carolina", "Florida", "Tampa Bay", "Washington", "Chicago", "Detroit", "Nashville", "St. Louis", "Calgary", "Colorado", "Edmonton", "Vancouver", "Anaheim", "Dallas", "Los Angeles", "San Jose", "Columbus", "Minnesota", "Winnipeg", "Arizona", "Vegas", "Seattle"]
    assert [team.name for team in teams] == ["Devils", "Islanders", "Rangers", "Flyers", "Penguins", "Bruins", "Sabres", "Canadiens", "Senators", "Maple Leafs", "Hurricanes", "Panthers", "Lightning", "Capitals", "Blackhawks", "Red Wings", "Predators", "Blues", "Flames", "Avalanche", "Oilers", "Canucks", "Ducks", "Stars", "Kings", "Sharks", "Blue Jackets", "Wild", "Jets", "Coyotes", "Golden Knights", "Kraken"]
    assert [team.abbreviation for team in teams] == ["NJD", "NYI", "NYR", "PHI", "PIT", "BOS", "BUF", "MTL", "OTT", "TOR", "CAR", "FLA", "TBL", "WSH", "CHI", "DET", "NSH", "STL", "CGY", "COL", "EDM", "VAN", "ANA", "DAL", "LAK", "SJS", "CBJ", "MIN", "WPG", "ARI", "VGK", "SEA"]
    assert [team.first_year for team in teams] == [1982, 1972, 1926, 1967, 1967, 1924, 1970, 1909, 1990, 1917, 1979, 1993, 1991, 1974, 1926, 1926, 1997, 1967, 1980, 1979, 1979, 1970, 1993, 1967, 1967, 1990, 1997, 1997, 2011, 1979, 2016, 2021]
    assert [team.division.id for team in teams] == [18, 18, 18, 18, 18, 17, 17, 17, 17, 17, 18, 17, 17, 18, 16, 17, 16, 16, 15, 16, 15, 15, 15, 16, 15, 15, 18, 16, 16, 16, 15, 15]
    assert [team.division.name for team in teams] == ["Metropolitan", "Metropolitan", "Metropolitan", "Metropolitan", "Metropolitan", "Atlantic", "Atlantic", "Atlantic", "Atlantic", "Atlantic", "Metropolitan", "Atlantic", "Atlantic", "Metropolitan", "Central", "Atlantic", "Central", "Central", "Pacific", "Central", "Pacific", "Pacific", "Pacific", "Central", "Pacific", "Pacific", "Metropolitan", "Central", "Central", "Central", "Pacific", "Pacific"]
    assert [team.division.name_short for team in teams] == ["Metro", "Metro", "Metro", "Metro", "Metro", "ATL", "ATL", "ATL", "ATL", "ATL", "Metro", "ATL", "ATL", "Metro", "CEN", "ATL", "CEN", "CEN", "PAC", "CEN", "PAC", "PAC", "PAC", "CEN", "PAC", "PAC", "Metro", "CEN", "CEN", "CEN", "PAC", "PAC"]
    assert [team.division.abbreviation for team in teams] == ["M", "M", "M", "M", "M", "A", "A", "A", "A", "A", "M", "A", "A", "M", "C", "A", "C", "C", "P", "C", "P", "P", "P", "C", "P", "P", "M", "C", "C", "C", "P", "P"]
    assert [team.conference.id for team in teams] == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 5, 5, 5, 5, 5]
    assert [team.conference.name for team in teams] == ["Eastern", "Eastern", "Eastern", "Eastern", "Eastern", "Eastern", "Eastern", "Eastern", "Eastern", "Eastern", "Eastern", "Eastern", "Eastern", "Eastern", "Western", "Eastern", "Western", "Western", "Western", "Western", "Western", "Western", "Western", "Western", "Western", "Western", "Eastern", "Western", "Western", "Western", "Western", "Western"]
    assert [team.conference.name_short for team in teams] == ["East", "East", "East", "East", "East", "East", "East", "East", "East", "East", "East", "East", "East", "East", "West", "East", "West", "West", "West", "West", "West", "West", "West", "West", "West", "West", "East", "West", "West", "West", "West", "West"]
    assert [team.conference.abbreviation for team in teams] == ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "W", "E", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "E", "W", "W", "W", "W", "W"]
    assert [team.franchise.id for team in teams] == [23, 22, 10, 16, 17, 6, 19, 1, 30, 5, 26, 33, 31, 24, 11, 12, 34, 18, 21, 27, 25, 20, 32, 15, 14, 29, 36, 37, 35, 28, 38, 39]
    assert [team.franchise.name for team in teams] == ["Devils", "Islanders", "Rangers", "Flyers", "Penguins", "Bruins", "Sabres", "Canadiens", "Senators", "Maple Leafs", "Hurricanes", "Panthers", "Lightning", "Capitals", "Blackhawks", "Red Wings", "Predators", "Blues", "Flames", "Avalanche", "Oilers", "Canucks", "Ducks", "Stars", "Kings", "Sharks", "Blue Jackets", "Wild", "Jets", "Coyotes", "Golden Knights", "Kraken"]
