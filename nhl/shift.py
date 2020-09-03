"""
Module containing NHL shift objects
"""
from dataclasses import dataclass

from .flyweight import Flyweight
from .player import Player

@dataclass(frozen=True)
class Shift(Flyweight):
    """
    NHL shift object.

    This is the detailed docstring.
    """

    __slots__ = ["game_id", "player_id", "shift_id", "on", "off"]
    _instances = {}

    game_id: int
    """int: NHL statsapi unique game ID"""

    player_id: int
    """int: NHL statsapi unique player ID"""

    shift_id: int
    """int: Shift number for specified game"""

    on: int
    """Gametime: Shift start gametime"""

    off: int
    """Gametime: Shift end gametime"""

    @classmethod
    def _key(cls, game_id, player_id, shift_id, *args, **kwargs):
        return (game_id, player_id, shift_id)

    @classmethod
    def has_key(cls, game_id, player_id, shift_id):
        return super().has_key(game_id, player_id, shift_id)

    @classmethod
    def from_key(cls, game_id, player_id, shift_id):
        return super().from_key(game_id, player_id, shift_id)

    def __repr__(self):
        return "<nhl.Shift: {} {:02d}:{:02d} to {:02d}:{:02d}, {:>3d} s, ID {}.{}.{}>".format(self.on.period_str, *self.on.period_m_s, *self.off.period_m_s, self.length, self.game_id, self.player_id, self.shift_id)

    @property
    def player(self):
        return Player.from_key(self.player_id)

    @property
    def length(self):
        return self.off.sec - self.on.sec
