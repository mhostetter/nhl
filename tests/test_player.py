import dataclasses
import pytest

import nhl

def test_frozen():
    player = nhl.Player(1, "Alex Ovechkin", 8, "LW")
    with pytest.raises(dataclasses.FrozenInstanceError):
        player.id = 2
