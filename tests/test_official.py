"""
A pytest module to test the `nhl.Official` class.
"""
import dataclasses
import pytest

import nhl

# NOTE: Currently querying an official using https://statsapi.web.nhl.com/api/v1/people/xxxx does not return a
# valid result. To test parsing, we've excerpted a JSON chunk from a game.
JSON = {
    "id" : 2332,
    "fullName" : "Wes McCauley",
    "link" : "/api/v1/people/2332"
}


def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        nhl.Official()


def test_frozen():
    official = nhl._official.parse(JSON)
    with pytest.raises(dataclasses.FrozenInstanceError):
        official.id = 2


# def test_flyweight():
#     official_1 = nhl._official.parse(JSON)
#     official_2 = nhl._official.parse(JSON)
#     assert official_1 is official_2
#     assert official_1 == official_2


def test_fetch_and_parse():
    official = nhl._official.parse(JSON)
    assert official.id == 2332
    assert official.name == "Wes McCauley"
    assert official.first_name == "Wes"
    assert official.last_name == "McCauley"
