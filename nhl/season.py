"""
Module containing NHL season objects
"""
from dataclasses import dataclass

from .flyweight import Flyweight
from datetime import datetime


@dataclass(frozen=True)
class Season(Flyweight):
    """
    NHL season object.
    """

    __slots__ = ["id", "name", "regular_season_start_date", "regular_season_end_date", "season_end_date", "number_of_games", "ties_in_use", "olympics_participation", "conferences_in_use", "divisions_in_use", "wild_card_in_use"]
    _instances = {}

    id: int
    name: str
    regular_season_start_date: datetime
    regular_season_end_date: datetime
    season_end_date: datetime
    number_of_games: int
    ties_in_use: bool
    olympics_participation: bool
    conferences_in_use: bool
    divisions_in_use: bool
    wild_card_in_use: bool

    @classmethod
    def _key(cls, id, *args, **kwargs):
        return id

    @classmethod
    def has_key(cls, id):
        return super().has_key(id)

    @classmethod
    def from_key(cls, id):
        return super().from_key(id)

    def __repr__(self):
        return "<nhl.Season: {}, ID {}, Regular season start: {}, Season end: {}>".format(self.name, self.id, self.regular_season_start_date, self.season_end_date)
