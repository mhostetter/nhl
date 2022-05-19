"""
A pytest module to test the `nhl.Conference` class.
"""
import dataclasses
import pytest

import nhl


def test_fail_no_args():
    with pytest.raises(TypeError):
        nhl.Conference()


def test_frozen(mock_conferences):
    conference = nhl.statsapi.conference(6)
    with pytest.raises(dataclasses.FrozenInstanceError):
        conference.id = 2


# def test_flyweight(mock_conferences):
#     conference_1 = nhl.statsapi.conference(6)
#     conference_2 = nhl.statsapi.conference(6)
#     assert conference_1 is conference_2
#     assert conference_1 == conference_2


def test_fetch_and_parse(mock_conferences):
    conference = nhl.statsapi.conference(6)
    assert conference.id == 6
    assert conference.name == "Eastern"
    assert conference.name_short == "East"
    assert conference.abbreviation == "E"


def test_fetch_and_parse_all(mock_conferences):
    conferences = nhl.statsapi.conferences()
    assert [conference.id for conference in conferences] == [6, 5]
    assert [conference.name for conference in conferences] == ["Eastern", "Western"]
