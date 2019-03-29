import dataclasses
import datetime
import pytest

import nhl

def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        game = nhl.Game()

def make_game():
    return nhl.statsapi.game(2017030415)

def test_frozen():
    game = make_game()
    with pytest.raises(dataclasses.FrozenInstanceError):
        game.id = 2

def test_flyweight():
    game_1 = make_game()
    game_2 = make_game()
    assert game_1 is game_2
    assert game_1 == game_2

def test_values():
    game = make_game()
    assert game.id == 2017030415
    assert game.home.id == 54
    assert game.away.id == 15
    assert game.venue.id == 5178

    # Test event parsing
    assert game.events[160].game_id == 2017030415
    assert game.events[160].id == 160
    assert game.events[160].type == "GOAL"
    assert game.events[160].subtype == "SLAP_SHOT"
    assert game.events[160].time == nhl.Gametime(2, 614)
    assert game.events[160].location == nhl.Location(-82, -26)
    assert game.events[160].team.id == 15
    assert game.events[160].by[0].id == 8471214
    assert game.events[160].by[1].id == 8473563
    assert game.events[160].by[2].id == 8474590
    assert game.events[160].on.id == 8470594
