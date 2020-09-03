from dataclasses import dataclass

from .flyweight import Flyweight


@dataclass(frozen=True)
class Gametime(Flyweight):
    """
    NHL gametime object.

    This object represents a unique time of the game. There are convenience properties to convert
    the gametime into convenient formats.

    Parameters
    ----------
    period : int
        The period of the game.
    period_sec : int
        The number of elapsed seconds in the period.
    """

    __slots__ = ["period", "period_sec"]
    _instances = {}

    period: int
    """int: Game period. 1-3 for regulation. 4+ for overtime."""

    period_sec: int
    """int: Elapsed seconds of the period."""

    @classmethod
    def _key(cls, period, period_sec, *args, **kwargs):
        return (period, period_sec)

    @classmethod
    def has_key(cls, period, period_sec):
        return super().has_key(period, period_sec)

    @classmethod
    def from_key(cls, period, period_sec):
        return super().from_key(period, period_sec)

    def __repr__(self):
        return "<nhl.Gametime: {} {:02d}:{:02d}>".format(self.period_str, *self.period_min_sec)

    @property
    def sec(self):
        """int: Elapsed seconds of the game."""
        return (self.period - 1)*20*60 + self.period_sec

    @property
    def min_sec(self):
        """(int, int): Elapsed minutes and seconds of the game."""
        return (self.sec // 60, self.sec % 60)

    @property
    def period_str(self):
        """str: Period number as string (i.e. "2nd")"""
        if self.period == 1:
            return "1st"
        elif self.period == 2:
            return "2nd"
        elif self.period == 3:
            return "3rd"
        else:
            return "{}th".format(self.period)

    @property
    def period_min_sec(self):
        """(int, int): Elapsed minutes and seconds of the period."""
        return (self.period_sec // 60, self.period_sec % 60)
