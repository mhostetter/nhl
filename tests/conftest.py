import os
import pytest

directory = os.path.dirname(__file__)

@pytest.fixture
def http_mock(requests_mock):
    text = open(os.path.join(directory, "data/conference_6.json")).read()
    requests_mock.get("http://statsapi.web.nhl.com/api/v1/conferences/6", text=text)

    text = open(os.path.join(directory, "data/division_18.json")).read()
    requests_mock.get("http://statsapi.web.nhl.com/api/v1/divisions/18", text=text)

    text = open(os.path.join(directory, "data/franchise_24.json")).read()
    requests_mock.get("http://statsapi.web.nhl.com/api/v1/franchises/24", text=text)

    text = open(os.path.join(directory, "data/game_2017030415.json")).read()
    requests_mock.get("http://statsapi.web.nhl.com/api/v1/game/2017030415/feed/live", text=text)

    text = open(os.path.join(directory, "data/player_8471214.json")).read()
    requests_mock.get("http://statsapi.web.nhl.com/api/v1/people/8471214", text=text)

    text = open(os.path.join(directory, "data/team_15.json")).read()
    requests_mock.get("http://statsapi.web.nhl.com/api/v1/teams/15", text=text)

    text = open(os.path.join(directory, "data/teams.json")).read()
    requests_mock.get("http://statsapi.web.nhl.com/api/v1/teams", text=text)

    text = open(os.path.join(directory, "data/venue_5094.json")).read()
    requests_mock.get("http://statsapi.web.nhl.com/api/v1/venues/5094", text=text)
