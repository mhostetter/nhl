"""
Module containing NHL player objects
"""
from dataclasses import dataclass
import datetime

from .list import List
from .player import Player


@dataclass(frozen=True)
class PlayerStats:
    """
    NHL player statistics.

    This is the detailed docstring.
    """

    __slots__ = ["player", "shifts", "events"]

    player: Player
    """Player: Player object"""

    shifts: List
    """List[Shift]: Player's shifts"""

    events: List
    """List[Event]: Player's events"""
