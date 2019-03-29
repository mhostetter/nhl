import dataclasses
import pytest

import nhl

def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        venue = nhl.Venue()

def make_venue():
    return nhl.statsapi.venue(5094)

def test_frozen():
    venue = make_venue()
    with pytest.raises(dataclasses.FrozenInstanceError):
        venue.id = 2

def test_flyweight():
    venue_1 = make_venue()
    venue_2 = make_venue()
    assert venue_1 is venue_2
    assert venue_1 == venue_2

def test_values():
    venue = make_venue()
    assert venue.id == 5094
    assert venue.name == "Capital One Arena"
