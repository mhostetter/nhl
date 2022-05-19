"""
A pytest module to test the `nhl.Division` class.
"""
import dataclasses
import pytest

import nhl


def test_fail_no_args():
    with pytest.raises(TypeError):
        nhl.Division()


def test_frozen(mock_divisions):
    division = nhl.statsapi.division(18)
    with pytest.raises(dataclasses.FrozenInstanceError):
        division.id = 2


# def test_flyweight(mock_divisions):
#     division_1 = nhl.statsapi.division(18)
#     division_2 = nhl.statsapi.division(18)
#     assert division_1 is division_2
#     assert division_1 == division_2


def test_fetch_and_parse(mock_divisions):
    division = nhl.statsapi.division(18)
    assert division.id == 18
    assert division.name == "Metropolitan"
    assert division.name_short == "Metro"
    assert division.abbreviation == "M"


def test_fetch_and_parse_all(mock_divisions):
    divisions = nhl.statsapi.divisions()
    assert [division.id for division in divisions] == [17, 16, 18, 15]
    assert [division.name for division in divisions] == ["Atlantic", "Central", "Metropolitan", "Pacific"]
    assert [division.name_short for division in divisions] == ["ATL", "CEN", "Metro", "PAC"]
    assert [division.abbreviation for division in divisions] == ["A", "C", "M", "P"]
