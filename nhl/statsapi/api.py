from datetime import datetime, timedelta
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


def schedule(schedule_date=datetime.now().strftime("%Y-%m-%d"), team_id=None):
    json = requests.get("{}/schedule?date={}&hydrate=team,division{}".format(BASE, schedule_date, ("&teamId=" + str(team_id)) if team_id else "")).json()
    if len(json["dates"]):
        return parse.parse_schedule(json["dates"][0])
    else:
        return parse.parse_schedule({"date": schedule_date, "games": []})


def season(date_str=datetime.now().strftime("%Y-%m-%d"), pre_season_allowance_days=30):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    all_seasons = seasons()
    given_year = date.strftime("%Y")
    relevant_seasons = all_seasons.filter("id", given_year, "contains")
    in_season = next((x for x in relevant_seasons if date >= x.regular_season_start_date - timedelta(days=pre_season_allowance_days) and date <= x.season_end_date), None)
    if in_season:
        return in_season
    return (
        relevant_seasons[0]
        if (
            date - relevant_seasons[0].season_end_date
            < (
                relevant_seasons[1].regular_season_start_date
                - timedelta(days=pre_season_allowance_days)
            ) - date
        )
        else relevant_seasons[1]
    )


def seasons(ids=None):
    json = requests.get("{}/seasons".format(BASE)).json()
    if ids:
        return List([parse.parse_season(s) for s in json["seasons"] if s["seasonId"] in ids])
    else:
        return List([parse.parse_season(s) for s in json["seasons"]])


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
