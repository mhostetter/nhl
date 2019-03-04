import requests

from . import endpoints
from ..list import List
from . import parse

def fetch_conference(conference_id):
    assert isinstance(conference_id, int)
    url = "{}/conferences/{}".format(endpoints.BASE, conference_id)
    r = requests.get(url)
    conference = parse.parse_conference(r.json()["conferences"][0])
    return conference

def fetch_conferences(conference_ids):
    assert isinstance(conference_ids, list)
    return List([fetch_conference(id) for id in conference_ids])

def fetch_division(division_id):
    assert isinstance(division_id, int)
    url = "{}/divisions/{}".format(endpoints.BASE, division_id)
    r = requests.get(url)
    division = parse.parse_division(r.json()["divisions"][0])
    return division

def fetch_divisions(division_ids):
    assert isinstance(division_ids, list)
    return List([fetch_division(id) for id in division_ids])

def fetch_franchise(franchise_id):
    assert isinstance(franchise_id, int)
    url = "{}/franchises/{}".format(endpoints.BASE, franchise_id)
    r = requests.get(url)
    franchise = parse.parse_franchise(r.json()["franchises"][0])
    return franchise

def fetch_franchises(franchise_ids):
    assert isinstance(franchise_ids, list)
    return List([fetch_franchise(id) for id in franchise_ids])

def fetch_player(player_id):
    assert isinstance(player_id, int)
    url = "{}/people/{}".format(endpoints.BASE, player_id)
    r = requests.get(url)
    player = parse.parse_player(r.json()["people"][0])
    return player

def fetch_team(team_id):
    assert isinstance(team_id, int)
    url = "{}/teams/{}".format(endpoints.BASE, team_id)
    r = requests.get(url)
    team = parse.parse_team(r.json()["teams"][0])
    return team

def fetch_teams(team_ids):
    assert isinstance(team_ids, list)
    return List([fetch_team(id) for id in team_ids])

def fetch_players(player_ids):
    assert isinstance(player_ids, list)
    return List([fetch_player(id) for id in player_ids])

def fetch_venue(venue_id):
    assert isinstance(venue_id, int)
    url = "{}/venues/{}".format(endpoints.BASE, venue_id)
    r = requests.get(url)
    venue = parse.parse_venue(r.json()["venues"][0])
    return venue

def fetch_venues(venue_ids):
    assert isinstance(venue_ids, list)
    return List([fetch_venue(id) for id in venue_ids])
