"""
Module containing NHL game time objects
"""
from dataclasses import dataclass

from .flyweight import Flyweight

@dataclass(frozen=True)
class Gametime(Flyweight):
    """
    NHL game time object.

    This is the detailed docstring.
    """

    __slots__ = ["period", "period_s"]
    _instances = {}

    period: int
    """int: Game period"""

    period_s: int
    """int: Period elapsed seconds"""

    @classmethod
    def _key(cls, period, period_s, *args, **kwargs):
        return (period, period_s)

    @classmethod
    def has_key(cls, period, period_s):
        return super().has_key(period, period_s)

    @classmethod
    def from_key(cls, period, period_s):
        return super().from_key(period, period_s)

    def __repr__(self):
        return "<nhl.Gametime: {} {:02d}:{:02d}>".format(self.period_str, *self.period_m_s)

    @property
    def s(self):
        """int: Game elapsed seconds"""
        return (self.period - 1)*20*60 + self.period_s

    @property
    def m_s(self):
        """(int, int): Game elapsed minutes and seconds"""
        return (self.s // 60, self.s % 60)

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
    def period_m_s(self):
        """(int, int): Period elapsed minutes and seconds"""
        return (self.period_s // 60, self.period_s % 60)
