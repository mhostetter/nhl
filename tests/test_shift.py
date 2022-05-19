"""
A pytest module to test the `nhl.Shift` class.
"""
import dataclasses
import pytest

import nhl


def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        nhl.Shift()


def test_frozen(mock_shifts):
    shifts = nhl.statsapi.shifts(2017030415, 8471214)
    with pytest.raises(dataclasses.FrozenInstanceError):
        shifts[0].shift_id = 2


# def test_flyweight(mock_shifts):
#     shifts_1 = nhl.statsapi.shifts(2017030415, 8471214)
#     shifts_2 = nhl.statsapi.shifts(2017030415, 8471214)
#     assert shifts_1 is shifts_2
#     assert shifts_1 == shifts_2


def test_fetch_and_parse(mock_shifts):
    shifts = nhl.statsapi.shifts(2017030415, 8471214)

    assert [shift.game_id for shift in shifts] == [2017030415,]*24
    assert [shift.player_id for shift in shifts] == [8471214,]*24
    assert [shift.shift_id for shift in shifts] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    assert [shift.on.sec for shift in shifts] == [27, 203, 414, 540, 701, 882, 1008, 1116, 1221, 1372, 1584, 1780, 1890, 2029, 2069, 2221, 2485, 2513, 2663, 2737, 2920, 3078, 3250, 3403]
    assert [shift.off.sec for shift in shifts] == [75, 254, 428, 605, 808, 927, 1034, 1180, 1321, 1399, 1650, 1814, 1912, 2049, 2120, 2266, 2508, 2558, 2717, 2851, 2970, 3106, 3292, 3453]
    assert [shift.length for shift in shifts] == [48, 51, 14, 65, 107, 45, 26, 64, 100, 27, 66, 34, 22, 20, 51, 45, 23, 45, 54, 114, 50, 28, 42, 50]


def test_exceptions(mock_shifts):
    with pytest.raises(ValueError):
        nhl.statsapi.shifts(2017030415, 8471675)
