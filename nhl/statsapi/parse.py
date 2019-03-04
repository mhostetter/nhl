import datetime

from ..conference import Conference
from ..division import Division
from ..franchise import Franchise
from ..player import Player
from ..team import Team
from ..venue import Venue

def parse_date(date_str):
    year = int(date_str.split("-")[0])
    month = int(date_str.split("-")[1])
    day = int(date_str.split("-")[2])
    return datetime.date(year, month, day)

def parse_height(height_str):
    feet = int(height_str.split("\' ")[0])
    inches = int(height_str.split("\' ")[1].split("\"")[0])
    return feet*12 + inches

def parse_conference(json):
    id = json["id"]
    if Conference.has_key(id): return Conference.from_key(id)
    name = json["name"]
    # NOTE: `nameShort` and `abbreviation` keys are not guaranteed. It depends on
    # which json object is returned.
    name_short = json.get("shortName", name[0:-3])
    abbreviation = json.get("abbreviation", name[0])
    return Conference(id, name, name_short, abbreviation)

def parse_division(json):
    id = json["id"]
    if Division.has_key(id): return Division.from_key(id)
    name = json["name"]
    name_short = json["nameShort"]
    abbreviation = json["abbreviation"]
    return Division(id, name, name_short, abbreviation)

def parse_franchise(json):
    id = json["franchiseId"]
    if Franchise.has_key(id): return Franchise.from_key(id)
    name = json["teamName"]
    return Franchise(id, name)

def parse_player(json):
    id = json["id"]
    if Player.has_key(id): return Player.from_key(id)
    name = json["fullName"]
    number = int(json["primaryNumber"])
    position = json["primaryPosition"]["abbreviation"]
    height = parse_height(json["height"])
    weight = json["weight"]
    shoots_catches = json["shootsCatches"]
    birth_date = parse_date(json["birthDate"])
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

def parse_venue(json):
    id = json["id"]
    if Venue.has_key(id): return Venue.from_key(id)
    name = json["name"]
    return Venue(id, name)
