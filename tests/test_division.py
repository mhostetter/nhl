"""
A pytest module to test the `nhl.Division` class.
"""
import dataclasses
import pytest

import nhl


def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        nhl.Division()


def test_frozen():
    division = nhl.statsapi.division(18)
    with pytest.raises(dataclasses.FrozenInstanceError):
        division.id = 2


# def test_flyweight():
#     division_1 = nhl.statsapi.division(18)
#     division_2 = nhl.statsapi.division(18)
#     assert division_1 is division_2
#     assert division_1 == division_2


def test_fetch_and_parse():
    division = nhl.statsapi.division(18)
    assert division.id == 18
    assert division.name == "Metropolitan"
    assert division.name_short == "Metro"
    assert division.abbreviation == "M"
