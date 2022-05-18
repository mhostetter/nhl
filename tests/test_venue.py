"""
A pytest module to test the `nhl.Venue` class.
"""
import dataclasses
import pytest

import nhl


def test_fail_no_args():
    with pytest.raises((IndexError, TypeError)):
        nhl.Venue()


def test_frozen(http_mock):
    venue = nhl.statsapi.venue(5094)
    with pytest.raises(dataclasses.FrozenInstanceError):
        venue.id = 2


# def test_flyweight(http_mock):
#     venue_1 = nhl.statsapi.venue(5094)
#     venue_2 = nhl.statsapi.venue(5094)
#     assert venue_1 is venue_2
#     assert venue_1 == venue_2


def test_fetch_and_parse(http_mock):
    venue = nhl.statsapi.venue(5094)
    assert venue.id == 5094
    assert venue.name == "Capital One Arena"


def test_fetch_and_parse_all(http_mock):
    venues = nhl.statsapi.venues()
    assert [venue.id for venue in venues] == [5076, 5064, 5098, 5030, 5019, 5059, 310, 5178, 5092, 5017, 5081, 5067, 5066, 5058, 5094, 5027, 5046]
    assert [venue.name for venue in venues] == ["Enterprise Center", "Ball Arena", "Xcel Energy Center", "Bridgestone Arena", "American Airlines Center", "Nationwide Arena", "NASSAU LIVE CENTER", "T-Mobile Arena", "United Center", "Amalie Arena", "STAPLES Center", "Prudential Center Map & Info", "PNC Arena", "Canada Life Centre", "Capital One Arena", "FLA Live Arena", "Honda Center"]
