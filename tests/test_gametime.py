import dataclasses
import pytest

import nhl

def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        gametime = nhl.Gametime()

def make_gametime():
    return nhl.Gametime(3, 314)

def test_frozen():
    gametime = make_gametime()
    with pytest.raises(dataclasses.FrozenInstanceError):
        gametime.period = 2

def test_flyweight():
    gametime_1 = make_gametime()
    gametime_2 = make_gametime()
    assert gametime_1 is gametime_2
    assert gametime_1 == gametime_2

def test_values():
    gametime = make_gametime()
    assert gametime.period == 3
    assert gametime.period_sec == 314
    assert gametime.period_min_sec == (5, 14)
    assert gametime.period_str == "3rd"
    assert gametime.sec == 2714
    assert gametime.min_sec == (45, 14)

def test_period_start_end():
    end_2nd = nhl.Gametime(2, 20*60)
    start_3rd = nhl.Gametime(3, 0*60)
    assert end_2nd is not start_3rd
    assert end_2nd.sec == start_3rd.sec
    assert end_2nd.min_sec == start_3rd.min_sec
