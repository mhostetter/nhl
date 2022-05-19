"""
A pytest module to test the `nhl.Player` class.
"""
import dataclasses
import pytest

import nhl


def test_fail_no_args():
    with pytest.raises(TypeError):
        nhl.Player()


def test_frozen(mock_people):
    player = nhl.statsapi.player(8471214)
    with pytest.raises(dataclasses.FrozenInstanceError):
        player.id = 2


# def test_flyweight(mock_people):
#     player_1 = nhl.statsapi.player(8471214)
#     player_2 = nhl.statsapi.player(8471214)
#     assert player_1 is player_2
#     assert player_1 == player_2


def test_fetch_and_parse(mock_people):
    player = nhl.statsapi.player(8471214)
    assert player.id == 8471214
    assert player.name == "Alex Ovechkin"
    assert player.first_name == "Alex"
    assert player.last_name == "Ovechkin"
    assert player.number == 8
    assert player.position == "LW"
    assert player.height == 75
    assert player.height_ft_in == (6, 3)
    assert player.weight == 238
    assert player.shoots_catches == "R"
    assert player.birth_date.year == 1985
    assert player.birth_date.month == 9
    assert player.birth_date.day == 17
    assert player.birth_city == "Moscow"
    assert player.birth_country == "RUS"
