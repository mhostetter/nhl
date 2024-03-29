"""
A module containing functions for querying the NHL statsapi REST API https://statsapi.web.nhl.com/api/v1.
"""
# pylint: disable=unused-import
from ._conference import conference, conferences
from ._division import division, divisions
from ._franchise import franchise, franchises
from ._player import player, players
from ._shift import shifts
from ._team import team, teams
from ._venue import venue, venues
