from ._location import Location

LENGTH = 200
"""Rink length (ft)"""

WIDTH = 85
"""Rink width (ft)"""

DX = LENGTH / 2
"""Delta length from center ice (ft)"""

DY = WIDTH / 2
"""Delta width from center ice (ft)"""

BLUE_LINE_X = 25
"""Blue line x-position from center ice (ft)"""

GOAL_LINE_X = 89
"""Goal line x-position from center ice (ft)"""

NZ_FACEOFF_DOT_X = 20
"""Neutral zone faceoff dot x-position from center ice (ft)"""

OZ_FACEOFF_DOT_X = 69
"""Offensive zone faceoff dot x-position from center ice (ft)"""

FACEOFF_DOT_Y = 22
"""All faceoff dot y-position from center ice (ft)"""

FACEOFF_DOTS = (
    (0, 0),
    ( NZ_FACEOFF_DOT_X,  FACEOFF_DOT_Y),
    ( NZ_FACEOFF_DOT_X, -FACEOFF_DOT_Y),
    (-NZ_FACEOFF_DOT_X,  FACEOFF_DOT_Y),
    (-NZ_FACEOFF_DOT_X, -FACEOFF_DOT_Y),
    ( OZ_FACEOFF_DOT_X,  FACEOFF_DOT_Y),
    ( OZ_FACEOFF_DOT_X, -FACEOFF_DOT_Y),
    (-OZ_FACEOFF_DOT_X,  FACEOFF_DOT_Y),
    (-OZ_FACEOFF_DOT_X, -FACEOFF_DOT_Y)
)
"""Tuple of faceoff dots (x, y)"""

HOME_GOAL_X = GOAL_LINE_X
HOME_GOAL_Y = 0
HOME_GOAL = Location(HOME_GOAL_X, HOME_GOAL_Y)

AWAY_GOAL_X = -GOAL_LINE_X
AWAY_GOAL_Y = 0
AWAY_GOAL = Location(AWAY_GOAL_X, AWAY_GOAL_Y)
