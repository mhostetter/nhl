"""
A pytest module to test the `nhl.Franchise` class.
"""
import dataclasses
import pytest

import nhl


def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        nhl.Franchise()


def test_frozen():
    franchise = nhl.statsapi.franchise(24)
    with pytest.raises(dataclasses.FrozenInstanceError):
        franchise.id = 2


# def test_flyweight():
#     franchise_1 = nhl.statsapi.franchise(24)
#     franchise_2 = nhl.statsapi.franchise(24)
#     assert franchise_1 is franchise_2
#     assert franchise_1 == franchise_2


def test_fetch_and_parse():
    franchise = nhl.statsapi.franchise(24)
    assert franchise.id == 24
    assert franchise.name == "Capitals"
