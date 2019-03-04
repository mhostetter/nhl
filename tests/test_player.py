import dataclasses
import datetime
import pytest

import nhl

def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        player = nhl.Player()

def make_player():
    return nhl.Player(8471214, "Alex Ovechkin", 8, "LW", 75, 235, "R",
        datetime.date(1985, 9, 17), "Moscow", "RUS")

def test_frozen():
    player = make_player()
    with pytest.raises(dataclasses.FrozenInstanceError):
        player.id = 2

def test_flyweight():
    player_1 = make_player()
    player_2 = make_player()
    assert player_1 is player_2
    assert player_1 == player_2

def test_name_parse():
    player = make_player()
    assert player.first_name == "Alex"
    assert player.last_name == "Ovechkin"

def test_height_convert():
    player = make_player()
    assert player.height == 75
    assert player.height_ft == 6
    assert player.height_in == 3

def test_birth_date_parse():
    player = make_player()
    assert isinstance(player.birth_date, datetime.date)
    assert player.birth_date.year == 1985
    assert player.birth_date.month == 9
    assert player.birth_date.day == 17
