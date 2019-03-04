import dataclasses
import pytest

import nhl

def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        conference = nhl.Conference()

def make_conference():
    return nhl.Conference(6, "Eastern", "East", "E")

def test_frozen():
    conference = make_conference()
    with pytest.raises(dataclasses.FrozenInstanceError):
        conference.id = 2

def test_flyweight():
    conference_1 = make_conference()
    conference_2 = make_conference()
    assert conference_1 is conference_2
    assert conference_1 == conference_2
