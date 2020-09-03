"""
Module containing NHL event objects
"""
from dataclasses import dataclass

from .flyweight import Flyweight
from .gametime import Gametime
from .list import List
from .location import Location
from .player import Player
from .team import Team
from .venue import Venue

@dataclass(frozen=True)
class Event(Flyweight):
    """
    NHL event object.

    This is the detailed docstring.
    """

    __slots__ = ["game_id", "id", "type", "subtype", "gametime", "location", "value", "score", "by_player",
                 "on_player", "by_team", "on_team", "by_players_on_ice", "on_players_on_ice"]
    _instances = {}

    game_id: int
    id: int
    type: str
    subtype: str
    gametime: Gametime
    location: Location
    value: float
    score: tuple
    by_player: Player
    on_player: Player
    by_team: Team
    on_team: Team
    by_players_on_ice: List
    on_players_on_ice: List

    @classmethod
    def _key(cls, game_id, id, *args, **kwargs):
        return (game_id, id)

    @classmethod
    def has_key(cls, game_id, id):
        return super().has_key(game_id, id)

    @classmethod
    def from_key(cls, game_id, id):
        return super().from_key(game_id, id)

    def __repr__(self):
        if self.type in ["GAME_SCHEDULED", "PERIOD_READY", "PERIOD_START", "STOPPAGE", "PERIOD_END", "PERIOD_OFFICIAL", "GAME_END", "GAME_OFFICIAL"]:
            return "<nhl.Event: {} {:02d}:{:02d}, {}, ID {}.{}>".format(self.gametime.period_str, *self.gametime.period_m_s, self.name, self.game_id, self.id)
        elif self.by_player is None:
            return "<nhl.Event: {} {:02d}:{:02d}, {:>2} {} on {} = {}, {}, {}, ID {}.{}>".format(self.gametime.period_str, *self.gametime.period_m_s, self.lead, self.by_strength, self.on_strength, self.strength, self.name, self.by_team.abbreviation, self.game_id, self.id)
        else:
            return "<nhl.Event: {} {:02d}:{:02d}, {:>2} {} on {} = {}, {}, {} {:>2} {:<2} {}, ID {}.{}>".format(self.gametime.period_str, *self.gametime.period_m_s, self.lead, self.by_strength, self.on_strength, self.strength, self.name, self.by_team.abbreviation, self.by_player.position, self.by_player.number, self.by_player.last_name, self.game_id, self.id)

        # # if self.type in ["GAME_SCHEDULED", "PERIOD_READY", "PERIOD_START", "STOP", "PERIOD_END", "PERIOD_OFFICIAL", "GAME_END", "GAME_OFFICIAL"]:
        # #     return "<nhl.Event: {} {:02d}:{:02d}, {}, ID {}.{}>".format(self.time.period_str, *self.time.period_m_s, self.type, self.game_id, self.id)
        # # elif self.by is None:
        # #     return "<nhl.Event: {} {:02d}:{:02d}, {:>2} {} on {} = {}, {}, {}, ID {}.{}>".format(self.time.period_str, *self.time.period_m_s, self.lead, self.by_strength, self.on_strength, self.strength, self.name, self.by_team.abbreviation, self.game_id, self.id)
        # # else:
        # #     return "<nhl.Event: {} {:02d}:{:02d}, {:>2} {} on {} = {}, {}, {} {:>2} {:<2} {}, ID {}.{}>".format(self.time.period_str, *self.time.period_m_s, self.lead, self.by_strength, self.on_strength, self.strength, self.name, self.by_team.abbreviation, self.by_player.position, self.by_player.number, self.by_player.last_name, self.game_id, self.id)
        # return "<nhl.Event: {} {:02d}:{:02d}, {}{}, ID {}.{}>".format(self.time.period_str, *self.time.period_m_s,
        #     self.type, " ({})".format(self.subtype) if self.subtype else "", self.game_id, self.id)

    @property
    def name(self):
        return self.type + self.subname

    @property
    def subname(self):
        return " ({}{})".format(self.subtype, ", {}".format(self.valuename) if self.value else "") if self.subtype else ""

    @property
    def valuename(self):
        if self.type == "PENALTY":
            return "{} min".format(self.value) if self.value else ""
        elif self.type in ["BLOCKED_SHOT", "MISSED_SHOT", "SHOT", "SAVE", "GOAL", "GOAL_AGAINST"]:
            return "{:1.0f} ft".format(self.value) if self.value else ""
        else:
            return ""

    @property
    def lead(self):
        return self.score[0] - self.score[1] if self.score[0] is not None else None

    @property
    def by_strength(self):
        return self.by_players_on_ice.len

    @property
    def on_strength(self):
        return self.on_players_on_ice.len

    @property
    def strength(self):
        return self.by_strength - self.on_strength
