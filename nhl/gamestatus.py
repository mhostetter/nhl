from dataclasses import dataclass

from .flyweight import Flyweight


@dataclass(frozen=True)
class GameStatus(Flyweight):
    """
    NHL game status object.
    """

    __slots__ = ["id", "abstract_game_state", "detailed_state", "start_time_tbd"]
    _instances = {}

    id: int
    abstract_game_state: str
    detailed_state: str
    start_time_tbd: bool

    @classmethod
    def _key(cls, id, *args, **kwargs):
        return (id)

    @classmethod
    def has_key(cls, id):
        return super().has_key(id)

    @classmethod
    def from_key(cls, id):
        return super().from_key(id)

    def __repr__(self):
        return "<nhl.GameStatus: {}>".format(self.detailed_state)
