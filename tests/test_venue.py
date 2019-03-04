import dataclasses
import pytest

import nhl

def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        venue = nhl.Venue()

def make_venue():
    return nhl.Venue(5094, "Capital One Arena")

def test_frozen():
    venue = make_venue()
    with pytest.raises(dataclasses.FrozenInstanceError):
        venue.id = 2

def test_flyweight():
    venue_1 = make_venue()
    venue_2 = make_venue()
    assert venue_1 is venue_2
    assert venue_1 == venue_2
