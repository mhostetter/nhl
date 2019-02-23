import dataclasses
import datetime
import pytest

import nhl

def test_fail_no_args():
    with pytest.raises(TypeError):
        player = nhl.Player()

def test_frozen():
    player = nhl.Player(1, "Alex Ovechkin", 8, "LW")
    with pytest.raises(dataclasses.FrozenInstanceError):
        player.id = 2

def test_name_parse():
    player = nhl.Player(1, "Alex Ovechkin", 8, "LW")
    assert player.first_name == "Alex"
    assert player.last_name == "Ovechkin"

def test_height_convert():
    player = nhl.Player(1, "Alex Ovechkin", 8, "LW")
    assert player.height is None
    assert player.height_ft is None
    assert player.height_in is None

    player = nhl.Player(1, "Alex Ovechkin", 8, "LW", height=75)
    assert player.height == 75
    assert player.height_ft == 6
    assert player.height_in == 3

def test_birth_date_parse():
    player = nhl.Player(1, "Alex Ovechkin", 8, "LW", birth_date_str="1985-09-17")
    assert isinstance(player.birth_date, datetime.date)
    assert player.birth_date.year == 1985
    assert player.birth_date.month == 9
    assert player.birth_date.day == 17
