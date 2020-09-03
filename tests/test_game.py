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
    assert game.info.id == 2017030415
    assert game.info.venue.id == 5178
    assert game.home.id == 54
    assert game.away.id == 15

    # Test event parsing for goal
    event = game.events.filter("id", 1600)[0]
    assert event.game_id == 2017030415
    assert event.id == 1600
    assert event.type == "GOAL"
    assert event.subtype == "SLAP_SHOT"
    assert event.gametime == nhl.Gametime(2, 614)
    assert event.location == nhl.Location(82, 26)
    assert event.by_team.id == 15
    assert event.by_player.id == 8471214
    assert event.on_player.id == 8470594

    # Test event parsing for primary assist
    event = game.events.filter("id", 1601)[0]
    assert event.game_id == 2017030415
    assert event.id == 1601
    assert event.type == "ASSIST"
    assert event.subtype == "PRIMARY"
    assert event.gametime == nhl.Gametime(2, 614)
    assert event.location == nhl.Location(82, 26)
    assert event.by_team.id == 15
    assert event.by_player.id == 8473563
    assert event.on_player.id == 8470594

    # Test event parsing for secondary assist
    event = game.events.filter("id", 1602)[0]
    assert event.game_id == 2017030415
    assert event.id == 1602
    assert event.type == "ASSIST"
    assert event.subtype == "SECONDARY"
    assert event.gametime == nhl.Gametime(2, 614)
    assert event.location == nhl.Location(82, 26)
    assert event.by_team.id == 15
    assert event.by_player.id == 8474590
    assert event.on_player.id == 8470594

