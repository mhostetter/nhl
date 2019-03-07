import dataclasses
import pytest

import nhl

def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        location = nhl.Location()

def make_location():
    return nhl.Location(-87, 23)

def test_frozen():
    location = make_location()
    with pytest.raises(dataclasses.FrozenInstanceError):
        location.x = 17

def test_flyweight():
    location_1 = make_location()
    location_2 = make_location()
    assert location_1 is location_2
    assert location_1 == location_2

def test_values():
    location = make_location()
    assert location.x == -87
    assert location.y == 23
