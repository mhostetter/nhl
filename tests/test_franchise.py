"""
A pytest module to test the `nhl.Franchise` class.
"""
import dataclasses
import pytest

import nhl


def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        nhl.Franchise()


def test_frozen(mock_franchises):
    franchise = nhl.statsapi.franchise(24)
    with pytest.raises(dataclasses.FrozenInstanceError):
        franchise.id = 2


# def test_flyweight(mock_franchises):
#     franchise_1 = nhl.statsapi.franchise(24)
#     franchise_2 = nhl.statsapi.franchise(24)
#     assert franchise_1 is franchise_2
#     assert franchise_1 == franchise_2


def test_fetch_and_parse(mock_franchises):
    franchise = nhl.statsapi.franchise(24)
    assert franchise.id == 24
    assert franchise.name == "Capitals"


def test_fetch_and_parse_all(mock_franchises):
    franchises = nhl.statsapi.franchises()
    assert [franchise.id for franchise in franchises] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
    assert [franchise.name for franchise in franchises] == ["Canadiens", "Wanderers", "Eagles", "Tigers", "Maple Leafs", "Bruins", "Maroons", "Americans", "Quakers", "Rangers", "Blackhawks", "Red Wings", "Barons", "Kings", "Stars", "Flyers", "Penguins", "Blues", "Sabres", "Canucks", "Flames", "Islanders", "Devils", "Capitals", "Oilers", "Hurricanes", "Avalanche", "Coyotes", "Sharks", "Senators", "Lightning", "Ducks", "Panthers", "Predators", "Jets", "Blue Jackets", "Wild", "Golden Knights", "Kraken"]
