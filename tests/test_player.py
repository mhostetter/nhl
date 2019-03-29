import dataclasses
import datetime
import pytest

import nhl

def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        player = nhl.Player()

def make_player():
    return nhl.statsapi.player(8471214)

def test_frozen():
    player = make_player()
    with pytest.raises(dataclasses.FrozenInstanceError):
        player.id = 2

def test_flyweight():
    player_1 = make_player()
    player_2 = make_player()
    assert player_1 is player_2
    assert player_1 == player_2

def test_values():
    player = make_player()
    assert player.id == 8471214
    assert player.name == "Alex Ovechkin"
    assert player.first_name == "Alex"
    assert player.last_name == "Ovechkin"
    assert player.number == 8
    assert player.position == "LW"
    assert player.height == 75
    assert player.height_ft_in == (6, 3)
    assert player.weight == 235
    assert player.shoots_catches == "R"
    assert player.birth_date.year == 1985
    assert player.birth_date.month == 9
    assert player.birth_date.day == 17
    assert player.birth_city == "Moscow"
    assert player.birth_country == "RUS"
