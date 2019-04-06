import requests

from .endpoints import BASE
from . import parse
from ..list import List


def conference(id):
    json = requests.get("{}/conferences/{}".format(BASE, id)).json()
    return parse.parse_conference(json["conferences"][0])


def conferences():
    json = requests.get("{}/conferences/{}".format(BASE, "")).json()
    return List(parse.parse_conference(item) for item in json["conferences"])


def division(id):
    json = requests.get("{}/divisions/{}".format(BASE, id)).json()
    return parse.parse_division(json["divisions"][0])


def divisions():
    json = requests.get("{}/divisions/{}".format(BASE, "")).json()
    return List(parse.parse_division(item) for item in json["divisions"])


def franchise(id):
    json = requests.get("{}/franchises/{}".format(BASE, id)).json()
    return parse.parse_franchise(json["franchises"][0])


def franchises():
    json = requests.get("{}/franchises/{}".format(BASE, "")).json()
    return List(parse.parse_franchise(item) for item in json["franchises"])


def game(id):
    json = requests.get("{}/game/{}/feed/live".format(BASE, id)).json()
    return parse.parse_game(json)


def player(id):
    json = requests.get("{}/people/{}".format(BASE, id)).json()
    return parse.parse_player(json["people"][0])


def players(ids):
    return List([player(id) for id in ids])


def team(id):
    json = requests.get("{}/teams/{}".format(BASE, id)).json()
    return parse.parse_team(json["teams"][0])


def teams(ids=None):
    if isinstance(ids, list):
        suffix = ",".join(map(str, ids))
        json = requests.get("{}/teams/?teamId={}".format(BASE, suffix)).json()
        return List(parse.parse_team(item) for item in json["teams"])
    else:
        json = requests.get("{}/teams/{}".format(BASE, "")).json()
        return List(parse.parse_team(item) for item in json["teams"])


def venue(id):
    json = requests.get("{}/venues/{}".format(BASE, id)).json()
    return parse.parse_venue(json["venues"][0])


def venues():
    json = requests.get("{}/venues/{}".format(BASE, "")).json()
    return List(parse.parse_venue(item) for item in json["venues"])
