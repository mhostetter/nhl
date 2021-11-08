"""
Module containing NHL schedule objects
"""
from dataclasses import dataclass

from datetime import datetime

from .flyweight import Flyweight
from .list import List


@dataclass(frozen=True)
class Schedule(Flyweight):
    """
    NHL schedule object.
    """

    __slots__ = ["schedule_date", "games"]
    _instances = {}

    schedule_date: datetime
    games: List

    @classmethod
    def _key(cls, schedule_date, *args, **kwargs):
        return schedule_date

    @classmethod
    def has_key(cls, schedule_date):
        return super().has_key(schedule_date)

    @classmethod
    def from_key(cls, schedule_date):
        return super().from_key(schedule_date)

    def __repr__(self):
        return "<nhl.Schedule: {}, {} games>".format(self.schedule_date, len(self.games))

    @property
    def num_games(self):
        return len(self.games)
