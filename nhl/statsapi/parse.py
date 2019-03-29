import datetime

from ..conference import Conference
from ..division import Division
from ..event import Event
from ..franchise import Franchise
from ..game import Game
from ..gametime import Gametime
from ..list import List
from ..location import Location
from ..player import Player
from ..team import Team
from ..venue import Venue

def _parse_date(date_str):
    year = int(date_str.split("-")[0])
    month = int(date_str.split("-")[1])
    day = int(date_str.split("-")[2])
    return datetime.date(year, month, day)

def _parse_height(height_str):
    feet = int(height_str.split("\' ")[0])
    inches = int(height_str.split("\' ")[1].split("\"")[0])
    return feet*12 + inches

def _parse_gametime(period_time):
    return 60*int(period_time.split(":")[0]) + int(period_time.split(":")[1])

def parse_conference(json):
    id = json["id"]
    if Conference.has_key(id): return Conference.from_key(id)
    name = json["name"]
    # NOTE: `nameShort` and `abbreviation` keys are not guaranteed. It depends on
    # which json object is returned.
    name_short = json.get("shortName", name[0:-3])
    abbreviation = json.get("abbreviation", name[0])
    return Conference(id, name, name_short, abbreviation)

def parse_conferences(json):
    return List([parse_conference(conference) for conference in json])

def parse_division(json):
    id = json["id"]
    if Division.has_key(id): return Division.from_key(id)
    name = json["name"]
    name_short = json["nameShort"]
    abbreviation = json["abbreviation"]
    return Division(id, name, name_short, abbreviation)

def parse_event(json, game_id):
    id = json["about"]["eventIdx"]
    if Event.has_key(game_id, id): return Event.from_key(game_id, id)
    type = json["result"]["eventTypeId"]
    if "secondaryType" in json["result"].keys():
        subtype = json["result"]["secondaryType"].upper().replace(" ", "_")
    else:
        subtype = None
    if "players" in json.keys():
        by = List()
        for i in range(0, len(json["players"]) - 1):
            by.append(Player.from_key(json["players"][i]["player"]["id"]))
        on = Player.from_key(json["players"][-1]["player"]["id"])
    else:
        by = None
        on = None
    period_seconds = _parse_gametime(json["about"]["periodTime"])
    time = Gametime(json["about"]["period"], period_seconds)
    location = parse_location(json["coordinates"])
    # NOTE: This is safe because the team has necessarily already been parsed and in memory
    if "team" in json.keys():
        team = Team.from_key(json["team"]["id"])
    else:
        team = None
    return Event(game_id, id, type, subtype, time, location, team, by, on)

def parse_franchise(json):
    id = json["franchiseId"]
    if Franchise.has_key(id): return Franchise.from_key(id)
    name = json["teamName"]
    return Franchise(id, name)

def parse_game(json):
    id = json["gamePk"]
    if Game.has_key(id): return Game.from_key(id)
    home = parse_team(json["gameData"]["teams"]["home"])
    away = parse_team(json["gameData"]["teams"]["away"])
    players = List([parse_player(p) for p in json["gameData"]["players"].values()])
    venue = parse_venue(json["gameData"]["venue"])
    events = List()
    for play in json["liveData"]["plays"]["allPlays"]:
        events.append(parse_event(play, id))
    return Game(id, home, away, venue, players, events)

def parse_location(json):
    if "x" in json.keys():
        return Location(int(json["x"]), int(json["y"]))
    else:
        return None

def parse_player(json):
    id = json["id"]
    if Player.has_key(id): return Player.from_key(id)
    name = json["fullName"]
    # NOTE: Occassionally this key is not provided
    _number = json.get("primaryNumber", None)
    number = int(_number) if _number else None
    position = json["primaryPosition"]["abbreviation"]
    height = _parse_height(json["height"])
    weight = json["weight"]
    shoots_catches = json["shootsCatches"]
    birth_date = _parse_date(json["birthDate"])
    birth_city = json["birthCity"]
    birth_country = json["birthCountry"]
    return Player(id, name, number, position, height, weight, shoots_catches,
        birth_date, birth_city, birth_country)

def parse_team(json):
    id = json["id"]
    if Team.has_key(id): return Team.from_key(id)
    location = json["locationName"]
    name = json["teamName"]
    abbreviation = json["abbreviation"]
    first_year = int(json["firstYearOfPlay"])
    division = parse_division(json["division"])
    conference = parse_conference(json["conference"])
    franchise = parse_franchise(json["franchise"])
    return Team(id, location, name, abbreviation, first_year, division, conference, franchise)

def parse_teams(json):
    return List([parse_team(team) for team in json])

def parse_venue(json):
    id = json["id"]
    if Venue.has_key(id): return Venue.from_key(id)
    name = json["name"]
    return Venue(id, name)
