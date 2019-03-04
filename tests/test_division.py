import dataclasses
import pytest

import nhl

def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        division = nhl.Division()

def make_division():
    return nhl.statsapi.fetch_division(18)

def test_frozen():
    division = make_division()
    with pytest.raises(dataclasses.FrozenInstanceError):
        division.id = 2

def test_flyweight():
    division_1 = make_division()
    division_2 = make_division()
    assert division_1 is division_2
    assert division_1 == division_2

def test_values():
    division = make_division()
    assert division.id == 18
    assert division.name == "Metropolitan"
    assert division.name_short == "Metro"
    assert division.abbreviation == "M"
