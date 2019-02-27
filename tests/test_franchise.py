import dataclasses
import datetime
import pytest

import nhl

def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        franchise = nhl.Franchise()

def make_franchise():
    return nhl.Franchise(24, "Capitals")

def test_frozen():
    franchise = make_franchise()
    with pytest.raises(dataclasses.FrozenInstanceError):
        franchise.id = 2

def test_flyweight():
    franchise_1 = make_franchise()
    franchise_2 = make_franchise()
    assert franchise_1 is franchise_2
    assert franchise_1 == franchise_2
