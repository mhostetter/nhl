"""
A module with functions to fetch/parse and a class to contain an NHL rink location.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, Optional

from ._overrides import set_module


def parse(json: Dict, period=1, flip=False) -> Location:
    """
    Parses the JSON response from the NHL statsapi. The period argument is used to normalize the left/right location of events.
    Flip is used to flip the location of events for all periods.
    """
    if "x" not in json:
        print("No 'x' found in dictionary")
        return Location()

    x = int(json["x"])
    y = int(json["y"])

    # This rink has the home start opposite of the convention. Flip the rink ends for all periods.
    if flip:
        x *= -1
        y *= -1

    # Flip the location of events during even periods so its as if the sides never switched. This makes
    # plotting easier.
    if period % 2 == 0:
        x *= -1
        y *= -1

    return Location(x, y)


@set_module("nhl")
@dataclass(frozen=True)
class Location:
    """
    NHL location object.
    """

    x: Optional[int] = None
    """Rink position in ft along x-axis (length) [-100, 100]"""

    y: Optional[int] = None
    """Rink position in ft along y-axis (breadth) [-42, 42]"""

    def __repr__(self):
        if self.x is None or self.y is None:
            return "<nhl.Location: None>"
        else:
            return f"<nhl.Location: {self.x:3.0f}, {self.y:3.0f}>"

    def distance(self, other):
        """
        Measure distance between current location and another on-ice location.

        Args:
            other (Location): location to measure distance from

        Returns:
            float: distance (ft)
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
