import os
import pytest

DIRECTORY = os.path.dirname(__file__)


@pytest.fixture
def mock_conferences(requests_mock):
    with open(os.path.join(DIRECTORY, "data/conferences.json"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://statsapi.web.nhl.com/api/v1/conferences/", text=text)
        requests_mock.get("https://statsapi.web.nhl.com/api/v1/conferences/", text=text)

    # Eastern
    with open(os.path.join(DIRECTORY, "data/conferences_6.json"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://statsapi.web.nhl.com/api/v1/conferences/6", text=text)
        requests_mock.get("https://statsapi.web.nhl.com/api/v1/conferences/6", text=text)


@pytest.fixture
def mock_divisions(requests_mock):
    with open(os.path.join(DIRECTORY, "data/divisions.json"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://statsapi.web.nhl.com/api/v1/divisions/", text=text)
        requests_mock.get("https://statsapi.web.nhl.com/api/v1/divisions/", text=text)

    # Metropolitan
    with open(os.path.join(DIRECTORY, "data/divisions_18.json"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://statsapi.web.nhl.com/api/v1/divisions/18", text=text)
        requests_mock.get("https://statsapi.web.nhl.com/api/v1/divisions/18", text=text)


@pytest.fixture
def mock_franchises(requests_mock):
    with open(os.path.join(DIRECTORY, "data/franchises.json"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://statsapi.web.nhl.com/api/v1/franchises/", text=text)
        requests_mock.get("https://statsapi.web.nhl.com/api/v1/franchises/", text=text)

    # Capitals
    with open(os.path.join(DIRECTORY, "data/franchises_24.json"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://statsapi.web.nhl.com/api/v1/franchises/24", text=text)
        requests_mock.get("https://statsapi.web.nhl.com/api/v1/franchises/24", text=text)


@pytest.fixture
def mock_people(requests_mock):
    # Ovechkin
    with open(os.path.join(DIRECTORY, "data/people_8471214.json"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://statsapi.web.nhl.com/api/v1/people/8471214", text=text)
        requests_mock.get("https://statsapi.web.nhl.com/api/v1/people/8471214", text=text)

    # Crosby
    with open(os.path.join(DIRECTORY, "data/people_8471675.json"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://statsapi.web.nhl.com/api/v1/people/8471675", text=text)
        requests_mock.get("https://statsapi.web.nhl.com/api/v1/people/8471675", text=text)


@pytest.fixture
def mock_teams(requests_mock):
    with open(os.path.join(DIRECTORY, "data/teams.json"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://statsapi.web.nhl.com/api/v1/teams/", text=text)
        requests_mock.get("https://statsapi.web.nhl.com/api/v1/teams/", text=text)

    # Capitals
    with open(os.path.join(DIRECTORY, "data/teams_15.json"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://statsapi.web.nhl.com/api/v1/teams/15", text=text)
        requests_mock.get("https://statsapi.web.nhl.com/api/v1/teams/15", text=text)


@pytest.fixture
def mock_venues(requests_mock):
    with open(os.path.join(DIRECTORY, "data/venues.json"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://statsapi.web.nhl.com/api/v1/venues/", text=text)
        requests_mock.get("https://statsapi.web.nhl.com/api/v1/venues/", text=text)

    # Capital One Arena
    with open(os.path.join(DIRECTORY, "data/venues_5094.json"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://statsapi.web.nhl.com/api/v1/venues/5094", text=text)
        requests_mock.get("https://statsapi.web.nhl.com/api/v1/venues/5094", text=text)


@pytest.fixture
def mock_shifts(requests_mock, mock_people):
    # 2018 Stanley Cup Final Game 5 home shifts (Golden Knights)
    with open(os.path.join(DIRECTORY, "data/20172018_TH030415.HTM"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://www.nhl.com/scores/htmlreports/20172018/TH030415.HTM", text=text)
        requests_mock.get("https://www.nhl.com/scores/htmlreports/20172018/TH030415.HTM", text=text)

    # 2018 Stanley Cup Final Game 5 away shifts (Capitals)
    with open(os.path.join(DIRECTORY, "data/20172018_TV030415.HTM"), encoding="utf-8") as f:
        text = f.read()
        requests_mock.get("http://www.nhl.com/scores/htmlreports/20172018/TV030415.HTM", text=text)
        requests_mock.get("https://www.nhl.com/scores/htmlreports/20172018/TV030415.HTM", text=text)


# @pytest.fixture
# def mock_game(requests_mock):
#     with open(os.path.join(DIRECTORY, "data/game_2017030415.json"), encoding="utf-8") as f:
#         text = f.read()
#         requests_mock.get("http://statsapi.web.nhl.com/api/v1/game/2017030415/feed/live", text=text)
#         requests_mock.get("https://statsapi.web.nhl.com/api/v1/game/2017030415/feed/live", text=text)
