import os
import pytest

directory = os.path.dirname(__file__)


@pytest.fixture
def http_mock(requests_mock):
    """
    Mocks the API endpoints so unit tests and CI don't overload the API webserver.
    """
    with open(os.path.join(directory, "data/conferences_6.json")) as f:
        text = f.read()
        requests_mock.get("http://statsapi.web.nhl.com/api/v1/conferences/6", text=text)
        requests_mock.get("https://statsapi.web.nhl.com/api/v1/conferences/6", text=text)

    # with open(os.path.join(directory, "data/division_18.json")) as f:
    #     text = f.read()
    #     requests_mock.get("http://statsapi.web.nhl.com/api/v1/divisions/18", text=text)
    #     requests_mock.get("https://statsapi.web.nhl.com/api/v1/divisions/18", text=text)

    # with open(os.path.join(directory, "data/franchise_24.json")) as f:
    #     text = f.read()
    #     requests_mock.get("http://statsapi.web.nhl.com/api/v1/franchises/24", text=text)
    #     requests_mock.get("https://statsapi.web.nhl.com/api/v1/franchises/24", text=text)

    # with open(os.path.join(directory, "data/game_2017030415.json")) as f:
    #     text = f.read()
    #     requests_mock.get("http://statsapi.web.nhl.com/api/v1/game/2017030415/feed/live", text=text)
    #     requests_mock.get("https://statsapi.web.nhl.com/api/v1/game/2017030415/feed/live", text=text)

    # with open(os.path.join(directory, "data/player_8471214.json")) as f:
    #     text = f.read()
    #     requests_mock.get("http://statsapi.web.nhl.com/api/v1/people/8471214", text=text)
    #     requests_mock.get("https://statsapi.web.nhl.com/api/v1/people/8471214", text=text)

    # with open(os.path.join(directory, "data/team_15.json")) as f:
    #     text = f.read()
    #     requests_mock.get("http://statsapi.web.nhl.com/api/v1/teams/15", text=text)
    #     requests_mock.get("https://statsapi.web.nhl.com/api/v1/teams/15", text=text)

    # with open(os.path.join(directory, "data/teams.json")) as f:
    #     text = f.read()
    #     requests_mock.get("http://statsapi.web.nhl.com/api/v1/teams", text=text)
    #     requests_mock.get("https://statsapi.web.nhl.com/api/v1/teams", text=text)

    # with open(os.path.join(directory, "data/venue_5094.json")) as f:
    #     text = f.read()
    #     requests_mock.get("http://statsapi.web.nhl.com/api/v1/venues/5094", text=text)
    #     requests_mock.get("https://statsapi.web.nhl.com/api/v1/venues/5094", text=text)
