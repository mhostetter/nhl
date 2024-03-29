"""
A Python 3 API for NHL game and player stats.
"""
from ._version import __version__

from . import rink
from . import statsapi

from ._conference import Conference
from ._division import Division
from ._event import Event
from ._franchise import Franchise
# from .game import Game
# from .gameinfo import GameInfo
from ._gametime import GameTime
# from .list import List
from ._location import Location
from ._official import Official
from ._player import Player
# from .playerstats import PlayerStats
from ._shift import Shift
from ._team import Team
from ._venue import Venue
