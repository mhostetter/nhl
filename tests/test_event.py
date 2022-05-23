"""
A pytest module to test the `nhl.Event` class.
"""
import dataclasses
import pytest

import nhl

GAME_ID = 2017030415
HOME_ID = 54
AWAY_ID = 15

JSON_HIT = {
    "players" : [ {
        "player" : {
            "id" : 8471214,
            "fullName" : "Alex Ovechkin",
            "link" : "/api/v1/people/8471214"
        },
        "playerType" : "Hitter"
    }, {
        "player" : {
            "id" : 8475188,
            "fullName" : "Brayden McNabb",
            "link" : "/api/v1/people/8475188"
        },
        "playerType" : "Hittee"
    } ],
    "result" : {
        "event" : "Hit",
        "eventCode" : "VGK418",
        "eventTypeId" : "HIT",
        "description" : "Alex Ovechkin hit Brayden McNabb"
    },
    "about" : {
        "eventIdx" : 170,
        "eventId" : 418,
        "period" : 2,
        "periodType" : "REGULAR",
        "ordinalNum" : "2nd",
        "periodTime" : "11:46",
        "periodTimeRemaining" : "08:14",
        "dateTime" : "2018-06-08T01:38:21Z",
        "goals" : {
            "away" : 2,
            "home" : 1
        }
    },
    "coordinates" : {
        "x" : -98.0,
        "y" : -9.0
    },
    "team" : {
        "id" : 15,
        "name" : "Washington Capitals",
        "link" : "/api/v1/teams/15",
        "triCode" : "WSH"
    }
}

JSON_GOAL = {
    "players": [
        {
            "player": {
                "id": 8471214,
                "fullName": "Alex Ovechkin",
                "link": "/api/v1/people/8471214"
            },
            "playerType": "Scorer",
            "seasonTotal": 15
        },
        {
            "player": {
                "id": 8473563,
                "fullName": "Nicklas Backstrom",
                "link": "/api/v1/people/8473563"
            },
            "playerType": "Assist",
            "seasonTotal": 18
        },
        {
            "player": {
                "id": 8474590,
                "fullName": "John Carlson",
                "link": "/api/v1/people/8474590"
            },
            "playerType": "Assist",
            "seasonTotal": 15
        },
        {
            "player": {
                "id": 8470594,
                "fullName": "Marc-Andre Fleury",
                "link": "/api/v1/people/8470594"
            },
            "playerType": "Goalie"
        }
    ],
    "result": {
        "event": "Goal",
        "eventCode": "VGK279",
        "eventTypeId": "GOAL",
        "description": "Alex Ovechkin (15) Slap Shot, assists: Nicklas Backstrom (18), John Carlson (15)",
        "secondaryType": "Slap Shot",
        "strength": {
            "code": "PPG",
            "name": "Power Play"
        },
        "gameWinningGoal": False,
        "emptyNet": False
    },
    "about": {
        "eventIdx": 160,
        "eventId": 279,
        "period": 2,
        "periodType": "REGULAR",
        "ordinalNum": "2nd",
        "periodTime": "10:14",
        "periodTimeRemaining": "09:46",
        "dateTime": "2018-06-08T01:33:50Z",
        "goals": {
            "away": 2,
            "home": 1
        }
    },
    "coordinates": {
        "x": -82.0,
        "y": -26.0
    },
    "team": {
        "id": 15,
        "name": "Washington Capitals",
        "link": "/api/v1/teams/15",
        "triCode": "WSH"
    }
}


def test_fail_no_args():
    with pytest.raises(TypeError):
        nhl.Event()


def test_frozen():
    events = nhl._event.parse(JSON_GOAL, GAME_ID, HOME_ID, AWAY_ID, False)
    with pytest.raises(dataclasses.FrozenInstanceError):
        events[0].id = 2


# def test_flyweight():
#     event_1 = nhl._event.parse(JSON_GOAL, GAME_ID, HOME_ID, AWAY_ID, False)
#     event_2 = nhl._event.parse(JSON_GOAL, GAME_ID, HOME_ID, AWAY_ID, False)
#     assert event_1 is event_2
#     assert event_1 == event_2


def test_parse_hit():
    event = nhl._event.parse(JSON_HIT, GAME_ID, HOME_ID, AWAY_ID, False)[0]
    assert event.game_id == 2017030415
    assert event.id == 1700
    assert event.type == "HIT"
    assert event.subtype is None
    assert event.time == nhl.GameTime(2, 706)
    assert event.location == nhl.Location(98, 9)
    assert event.score == (1, 2)
    assert event.by_player_id == 8471214
    assert event.on_player_id == 8475188
    assert event.by_team_id == 15
    assert event.on_team_id == 54


def test_parse_goal():
    events = nhl._event.parse(JSON_GOAL, GAME_ID, HOME_ID, AWAY_ID, False)
    assert [event.game_id for event in events] == [2017030415, 2017030415, 2017030415]
    assert [event.id for event in events] == [1602, 1601, 1600]
    assert [event.type for event in events] == ['ASSIST', 'ASSIST', 'GOAL']
    assert [event.subtype for event in events] == ['SECONDARY', 'PRIMARY', 'SLAP_SHOT']
    time = nhl.GameTime(2, 614)
    assert [event.time for event in events] == [time,]*3
    location = nhl.Location(82, 26)
    assert [event.location for event in events] == [location,]*3
    # assert [event.value for event in events] == [26.92582403567252,]*3
    assert [event.score for event in events] == [(1,2),]*3
    assert [event.by_player_id for event in events] == [8474590, 8473563, 8471214]
    assert [event.on_player_id for event in events] == [8470594, 8470594, 8470594]
    assert [event.by_team_id for event in events] == [15, 15, 15]
    assert [event.on_team_id for event in events] == [54, 54, 54]
