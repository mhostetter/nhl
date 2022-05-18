"""
A module with a class to represent a specific game time moment.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from ._overrides import set_module


@set_module("nhl")
@dataclass(frozen=True)
class GameTime:
    """
    NHL game time object.

    This object represents a unique time of the game. There are convenience properties to convert
    the game time into convenient formats.
    """

    __slots__ = ["period", "period_sec"]
    _instances = {}

    period: int
    """Game period. 1-3 for regulation. 4+ for overtime."""

    period_sec: int
    """Elapsed seconds of the period."""

    def __repr__(self):
        minute, second = self.period_min_sec
        return f"<nhl.GameTime: {self.period_str} {minute:02d}:{second:02d}>"

    @property
    def sec(self) -> int:
        """Elapsed seconds of the game."""
        return (self.period - 1)*20*60 + self.period_sec

    @property
    def min_sec(self) -> Tuple[int, int]:
        """Elapsed minutes and seconds of the game."""
        return (self.sec // 60, self.sec % 60)

    @property
    def period_str(self) -> str:
        """Period number as string (i.e. "2nd")"""
        if self.period == 1:
            return "1st"
        elif self.period == 2:
            return "2nd"
        elif self.period == 3:
            return "3rd"
        else:
            return f"{self.period}th"

    @property
    def period_min_sec(self) -> Tuple[int, int]:
        """Elapsed minutes and seconds of the period."""
        return (self.period_sec // 60, self.period_sec % 60)
