"""
A pytest module to test the `nhl.Location` class.
"""
import dataclasses
import math
import pytest

import nhl

# NOTE: Locations are dictionaries with key "coordinates".
JSON_1 = {
    "x" : -68.0,
    "y" : -11.0
}
JSON_2 = {}


def test_frozen():
    location = nhl._location.parse(JSON_1)
    with pytest.raises(dataclasses.FrozenInstanceError):
        location.x = 0


# def test_flyweight():
#     location_1 = nhl._location.parse(JSON)
#     location_2 = nhl._location.parse(JSON)
#     assert location_1 is location_2
#     assert location_1 == location_2


def test_and_parse():
    location = nhl._location.parse(JSON_1)
    assert isinstance(location.x, int)
    assert location.x == -68
    assert isinstance(location.y, int)
    assert location.y == -11


def test_parse_empty():
    location = nhl._location.parse(JSON_2)
    assert location.x is None
    assert location.y is None


def test_distance():
    location_1 = nhl.Location(-5, -50)
    location_2 = nhl.Location(10, 15)
    assert location_1.distance(location_2) == math.sqrt(15**2 + 65**2)
