"""
A module with functions to parse and a class to contain an NHL event.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple, List, Dict

from . import _location, rink
from ._gametime import GameTime, convert_gametime
from ._location import Location
from ._overrides import set_module

# Reword certain phrases in event subtype
SUBTYPE_CONVERSIONS = {
    "INTERFERENCE_GOALKEEPER": "GOALTENDER_INTERFERENCE",
    "HI_STICKING": "HIGH_STICKING",
    "HI_STICK_DOUBLE_MINOR": "HIGH_STICKING_DOUBLE_MINOR",
    "GOALPOST": "HIT_GOALPOST",
    "DELAYING_GAME_PUCK_OVER_GLASS": "DELAY_OF_GAME_PUCK_OVER_GLASS",
    "DELAY_GM_FACE_OFF_VIOLATION": "DELAY_OF_GAME_FACE_OFF_VIOLATION",
}


def parse(json: Dict, game_id: int, home_id: int, away_id: int, flip: bool) -> List[Event]:
    """
    Parses the JSON response from the NHL statsapi.
    """
    # pylint: disable=too-many-statements
    events = []

    id = json["about"]["eventIdx"]*10
    # if Event.has_key(game_id, id):
    #     return Event.from_key(game_id, id)

    type = json["result"]["eventTypeId"]

    # Create a subtype
    if type in ["STOP"]:
        type = "STOPPAGE"
        subtype = json["result"]["description"]
    elif type in ["MISSED_SHOT"]:
        subtype = json["result"]["description"].split(" - ")[1].upper()
    elif type in ["SHOT", "GOAL"]:
        subtype = json["result"]["secondaryType"].upper()
    else:
        subtype = json["result"].get("secondaryType", None)

    if subtype:
        subtype = convert_subtype(subtype)

    if "team" in json:
        if home_id == json["team"]["id"]:
            by_team_id, on_team_id = home_id, away_id
        else:
            # score = (score[1], score[0])
            by_team_id, on_team_id = away_id, home_id
    else:
        # score = (None, None)
        by_team_id, on_team_id = None, None

    score = (json["about"]["goals"]["home"], json["about"]["goals"]["away"])

    players = json.get("players", [])

    # The first player is the one that caused the event
    if len(players) > 0:
        by_player_id = players[0]["player"]["id"]
    else:
        by_player_id = None

    # The second player is the one that was affected by the event
    if len(players) > 1:
        on_player_id = players[-1]["player"]["id"]
    else:
        on_player_id = None

    # The 3rd+ player(s), if provided, are the assists on the goal
    if len(players) > 2:
        assist_player_ids = [p["player"]["id"] for p in players[1:-1]]
    else:
        assist_player_ids = []

    time = GameTime(json["about"]["period"], convert_gametime(json["about"]["periodTime"]))
    location = _location.parse(json["coordinates"], time.period, flip)

    # if "team" in json:
    #     # NOTE: This is safe because the team has necessarily already been parsed and is in memory
    #     team = Team.from_key(json["team"]["id"])
    # else:
    #     team = None

    if type in ["PENALTY"]:
        value = json["result"]["penaltyMinutes"]
    elif type in ["BLOCKED_SHOT"]:
        if on_team_id == home_id:
            value = location.distance(rink.AWAY_GOAL)
        else:
            value = location.distance(rink.HOME_GOAL)
    elif type in ["MISSED_SHOT", "SHOT", "GOAL"]:
        if by_team_id == home_id:
            value = location.distance(rink.AWAY_GOAL)
        else:
            value = location.distance(rink.HOME_GOAL)
    else:
        value = None

    # if by_team is None:
    #     home_players_on_ice = List()
    #     away_players_on_ice = List()
    # elif type in ["ASSIST", "GOAL", "PENALTY"]:
    #     home_players_on_ice = home_shifts.filter("on.sec", time.sec, "<").filter("off.sec", time.sec, ">=").sort("player_id")
    #     away_players_on_ice = away_shifts.filter("on.sec", time.sec, "<").filter("off.sec", time.sec, ">=").sort("player_id")
    # else:
    #     home_players_on_ice = home_shifts.filter("on.sec", time.sec, "<=").filter("off.sec", time.sec, ">").sort("player_id")
    #     away_players_on_ice = away_shifts.filter("on.sec", time.sec, "<=").filter("off.sec", time.sec, ">").sort("player_id")

    # if by_team is home:
    #     by_players_on_ice = home_players_on_ice
    #     on_players_on_ice = away_players_on_ice
    # else:
    #     by_players_on_ice = away_players_on_ice
    #     on_players_on_ice = home_players_on_ice

    # Process secondary assist if it was a goal
    if type == "GOAL" and len(assist_player_ids) >= 2:
        secondary_assist = Event(game_id, id + 2, "ASSIST", "SECONDARY", time, location, value, score, assist_player_ids[1], on_player_id, by_team_id, on_team_id)
        events.append(secondary_assist)

    # Process primary assist if it was a goal
    if type == "GOAL" and len(assist_player_ids) >= 1:
        primary_assist = Event(game_id, id + 1, "ASSIST", "PRIMARY", time, location, value, score, assist_player_ids[0], on_player_id, by_team_id, on_team_id)
        events.append(primary_assist)

    event = Event(game_id, id, type, subtype, time, location, value, score, by_player_id, on_player_id, by_team_id, on_team_id)
    events.append(event)

    return events


def convert_subtype(subtype: str) -> str:
    subtype = subtype.upper().replace(":", "")
    subtype = subtype.upper().replace(" ", "_")
    subtype = subtype.upper().replace("-", "_")
    subtype = subtype.upper().replace("___", "_")
    subtype = SUBTYPE_CONVERSIONS.get(subtype, subtype)
    return subtype


@set_module("nhl")
@dataclass(frozen=True)
class Event:
    """
    NHL event object.
    """

    game_id: int
    id: int
    type: str
    subtype: str
    time: GameTime
    location: Location
    value: float
    score: Tuple[int, int]
    by_player_id: int
    on_player_id: int
    by_team_id: int
    on_team_id: int
    # by_player: Player
    # on_player: Player
    # by_team: Team
    # on_team: Team
    # by_players_on_ice: List[Player]
    # on_players_on_ice: List[Player]

    # def __repr__(self):
    #     # pylint: disable=consider-using-f-string
    #     if self.type in ["GAME_SCHEDULED", "PERIOD_READY", "PERIOD_START", "STOPPAGE", "PERIOD_END", "PERIOD_OFFICIAL", "GAME_END", "GAME_OFFICIAL"]:
    #         return "<nhl.Event: {} {:02d}:{:02d}, {}, ID {}.{}>".format(self.time.period_str, *self.time.period_min_sec, self.name, self.game_id, self.id)
    #     elif self.by_player is None:
    #         return "<nhl.Event: {} {:02d}:{:02d}, {:>2} {} on {} = {}, {}, {}, ID {}.{}>".format(self.time.period_str, *self.time.period_min_sec, self.lead, self.by_strength, self.on_strength, self.strength, self.name, self.by_team.abbreviation, self.game_id, self.id)
    #     else:
    #         return "<nhl.Event: {} {:02d}:{:02d}, {:>2} {} on {} = {}, {}, {} {:>2} {:<2} {}, ID {}.{}>".format(self.time.period_str, *self.time.period_min_sec, self.lead, self.by_strength, self.on_strength, self.strength, self.name, self.by_team.abbreviation, self.by_player.position, self.by_player.number, self.by_player.last_name, self.game_id, self.id)

    #     # # if self.type in ["GAME_SCHEDULED", "PERIOD_READY", "PERIOD_START", "STOP", "PERIOD_END", "PERIOD_OFFICIAL", "GAME_END", "GAME_OFFICIAL"]:
    #     # #     return "<nhl.Event: {} {:02d}:{:02d}, {}, ID {}.{}>".format(self.time.period_str, *self.time.period_min_sec, self.type, self.game_id, self.id)
    #     # # elif self.by is None:
    #     # #     return "<nhl.Event: {} {:02d}:{:02d}, {:>2} {} on {} = {}, {}, {}, ID {}.{}>".format(self.time.period_str, *self.time.period_min_sec, self.lead, self.by_strength, self.on_strength, self.strength, self.name, self.by_team.abbreviation, self.game_id, self.id)
    #     # # else:
    #     # #     return "<nhl.Event: {} {:02d}:{:02d}, {:>2} {} on {} = {}, {}, {} {:>2} {:<2} {}, ID {}.{}>".format(self.time.period_str, *self.time.period_min_sec, self.lead, self.by_strength, self.on_strength, self.strength, self.name, self.by_team.abbreviation, self.by_player.position, self.by_player.number, self.by_player.last_name, self.game_id, self.id)
    #     # return "<nhl.Event: {} {:02d}:{:02d}, {}{}, ID {}.{}>".format(self.time.period_str, *self.time.period_min_sec,
    #     #     self.type, " ({})".format(self.subtype) if self.subtype else "", self.game_id, self.id)

    @property
    def name(self):
        return self.type + self.subname

    @property
    def subname(self):
        if self.subtype:
            value = f", {self.valuename}" if self.value else ""
            return f" ({self.subtype}{value})"
        else:
            return ""

    @property
    def valuename(self):
        if self.type == "PENALTY":
            return f"{self.value} min" if self.value else ""
        elif self.type in ["BLOCKED_SHOT", "MISSED_SHOT", "SHOT", "SAVE", "GOAL", "GOAL_AGAINST"]:
            return f"{self.value:1.0f} ft" if self.value else ""
        else:
            return ""

    @property
    def lead(self):
        if self.score[0] is not None:
            return self.score[0] - self.score[1]
        else:
            return None

    # @property
    # def by_strength(self):
    #     return self.by_players_on_ice.len

    # @property
    # def on_strength(self):
    #     return self.on_players_on_ice.len

    # @property
    # def strength(self):
    #     return self.by_strength - self.on_strength
