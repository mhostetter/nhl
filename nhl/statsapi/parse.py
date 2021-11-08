from bs4 import BeautifulSoup
import datetime
import requests

from ..conference import Conference
from ..division import Division
from ..event import Event
from ..franchise import Franchise
from ..game import Game
from ..gameinfo import GameInfo
from ..gametime import Gametime
from ..list import List
from ..location import Location
from ..official import Official
from ..player import Player
from ..playerstats import PlayerStats
from .. import rink
from ..shift import Shift
from ..team import Team
from ..venue import Venue


def _fetch_shifts(game_id, side):
    season_id = game_id // 1000000
    lower_game_id = game_id % 1000000
    side_id = "H" if side == "home" else "V"
    url = "http://www.nhl.com/scores/htmlreports/{:04d}{:04d}/T{:1s}{:06d}.HTM".format(season_id, season_id + 1, side_id, lower_game_id)
    print(url)
    result = requests.get(url)
    print(result)
    return result.text


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
    return List([parse_conference(j) for j in json])


def parse_division(json):
    id = json["id"]
    if Division.has_key(id): return Division.from_key(id)
    name = json["name"]
    name_short = json["nameShort"]
    abbreviation = json["abbreviation"]
    return Division(id, name, name_short, abbreviation)


def parse_events(json, info, home_score, away_score, home_shifts, away_shifts, flip_sides):
    id = json["about"]["eventIdx"]*10
    game_id = info.id
    if Event.has_key(game_id, id): return Event.from_key(game_id, id)

    type = json["result"]["eventTypeId"]
    if type in ["STOP"]:
        type = "STOPPAGE"
        subtype = json["result"]["description"]
    elif type in ["MISSED_SHOT"]:
        subtype = json["result"]["description"].split(" - ")[1].upper()
    elif type in ["SHOT", "GOAL"]:
        subtype = json["result"]["secondaryType"].upper()
    else:
        subtype = json["result"].get("secondaryType", None)

    if subtype:
        subtype = subtype.upper().replace(":", "")
        subtype = subtype.upper().replace(" ", "_")
        subtype = subtype.upper().replace("-", "_")
        subtype = subtype.upper().replace("___", "_")
        if subtype == "INTERFERENCE_GOALKEEPER":
            subtype = "GOALTENDER_INTERFERENCE"
        if subtype == "HI_STICKING":
            subtype = "HIGH_STICKING"
        if subtype == "HI_STICK_DOUBLE_MINOR":
            subtype = "HIGH_STICKING_DOUBLE_MINOR"
        if subtype == "GOALPOST":
            subtype = "HIT_GOALPOST"
        if subtype == "DELAYING_GAME_PUCK_OVER_GLASS":
            subtype = "DELAY_OF_GAME_PUCK_OVER_GLASS"
        if subtype == "DELAY_GM_FACE_OFF_VIOLATION":
            subtype = "DELAY_OF_GAME_FACE_OFF_VIOLATION"

    if "team" in json:
        if info.home_team.id == json["team"]["id"]:
            score = (home_score, away_score)
            by_team = info.home_team
            on_team = info.away_team
        else:
            score = (away_score, home_score)
            by_team = info.away_team
            on_team = info.home_team
    else:
        score = (None, None)
        by_team = None
        on_team = None

    players = json.get("players", [])
    if len(players) > 0:
        # NOTE: This is safe because the players have necessarily already been parsed and are in memory
        by_player = Player.from_key(players[0]["player"]["id"])
    else:
        by_player = None

    if len(players) > 1:
        # NOTE: This is safe because the players have necessarily already been parsed and are in memory
        on_player = Player.from_key(players[-1]["player"]["id"])
    else:
        on_player = None

    if len(players) > 2:
        # NOTE: This is safe because the players have necessarily already been parsed and are in memory
        assist_players = List([Player.from_key(p["player"]["id"]) for p in players[1:-1]])
    else:
        assist_players = List()

    gametime = Gametime(json["about"]["period"], _parse_gametime(json["about"]["periodTime"]))
    location = parse_location(json["coordinates"], gametime, flip_sides)

    # if "team" in json:
    #     # NOTE: This is safe because the team has necessarily already been parsed and is in memory
    #     team = Team.from_key(json["team"]["id"])
    # else:
    #     team = None

    if type in ["PENALTY"]:
        value = json["result"]["penaltyMinutes"]
    elif type in ["BLOCKED_SHOT"]:
        if on_team.id == info.home_team.id:
            value = location.distance(rink.AWAY_GOAL)
        else:
            value = location.distance(rink.HOME_GOAL)
    elif type in ["MISSED_SHOT", "SHOT", "GOAL"]:
        if by_team.id == info.home_team.id:
            value = location.distance(rink.AWAY_GOAL)
        else:
            value = location.distance(rink.HOME_GOAL)
    else:
        value = None

    if by_team is None:
        home_players_on_ice = List()
        away_players_on_ice = List()
    elif type in ["ASSIST", "GOAL", "PENALTY"]:
        home_players_on_ice = home_shifts.filter("on.sec", gametime.sec, "<").filter("off.sec", gametime.sec, ">=").sort("player_id")
        away_players_on_ice = away_shifts.filter("on.sec", gametime.sec, "<").filter("off.sec", gametime.sec, ">=").sort("player_id")
    else:
        home_players_on_ice = home_shifts.filter("on.sec", gametime.sec, "<=").filter("off.sec", gametime.sec, ">").sort("player_id")
        away_players_on_ice = away_shifts.filter("on.sec", gametime.sec, "<=").filter("off.sec", gametime.sec, ">").sort("player_id")

    if by_team is info.home_team:
        by_players_on_ice = home_players_on_ice
        on_players_on_ice = away_players_on_ice
    else:
        by_players_on_ice = away_players_on_ice
        on_players_on_ice = home_players_on_ice

    events = List()
    if type == "GOAL" and len(assist_players) >= 2:
        events.append(Event(game_id, id + 2, "ASSIST", "SECONDARY", gametime, location, value, score, assist_players[1], on_player, by_team, on_team, by_players_on_ice, on_players_on_ice))
    if type == "GOAL" and len(assist_players) >= 1:
        events.append(Event(game_id, id + 1, "ASSIST", "PRIMARY", gametime, location, value, score, assist_players[0], on_player, by_team, on_team, by_players_on_ice, on_players_on_ice))
    events.append(Event(game_id, id, type, subtype, gametime, location, value, score, by_player, on_player, by_team, on_team, by_players_on_ice, on_players_on_ice))
    return events
    # return Event(game_id, id, type, subtype, gametime, location, value, score, by_player, with_players, on_player, by_team, on_team, by_players_on_ice, on_players_on_ice)


def parse_franchise(json):
    id = json["franchiseId"]
    if Franchise.has_key(id): return Franchise.from_key(id)
    name = json["teamName"]
    return Franchise(id, name)


def parse_game(json):
    id = json["gamePk"]
    if Game.has_key(id): return Game.from_key(id)
    season_id = json["gameData"]["game"]["season"]
    game_type = json["gameData"]["game"]["type"]
    if game_type == "PR": game_type = "PRE_SEASON"
    elif game_type == "R": game_type = "REGULAR_SEASON"
    elif game_type == "P": game_type = "PLAYOFF"
    start_datetime = json["gameData"]["datetime"]["dateTime"]
    end_datetime = json["gameData"]["datetime"]["endDateTime"]

    venue = parse_venue(json["gameData"]["venue"])

    home_team = parse_team(json["gameData"]["teams"]["home"])
    away_team = parse_team(json["gameData"]["teams"]["away"])

    home_score = json["liveData"]["boxscore"]["teams"]["home"]["teamStats"]["teamSkaterStats"]["goals"]
    away_score = json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["goals"]

    referees = List()
    linesmen = List()
    for j in json["liveData"]["boxscore"]["officials"]:
        official = parse_official(j["official"])
        if j["officialType"] == "Referee":
            referees.append(official)
        elif j["officialType"] == "Linesman":
            linesmen.append(official)

    end_type = None
    end_gametime = None
    for j in json["liveData"]["plays"]["allPlays"]:
        if j["result"]["eventTypeId"] == "GAME_END":
            end_type = j["about"]["periodType"]
            end_gametime = Gametime(j["about"]["period"], _parse_gametime(j["about"]["periodTime"]))

    info = GameInfo(id, season_id, game_type, start_datetime, end_datetime, venue, home_team, away_team, (home_score, away_score), end_type, end_gametime, referees, linesmen)

    home_coach = json["liveData"]["boxscore"]["teams"]["home"]["coaches"][0]["person"]["fullName"] if len(json["liveData"]["boxscore"]["teams"]["home"]["coaches"]) >= 1 else None
    away_coach = json["liveData"]["boxscore"]["teams"]["away"]["coaches"][0]["person"]["fullName"] if len(json["liveData"]["boxscore"]["teams"]["away"]["coaches"]) >= 1 else None

    players = List([parse_player(j) for j in json["gameData"]["players"].values()])

    home_shifts = List()
    home_shifts_html = _fetch_shifts(id, "home")
    for j in json["liveData"]["boxscore"]["teams"]["home"]["players"].values():
        if j["person"]["id"] not in json["liveData"]["boxscore"]["teams"]["home"]["scratches"]:
            player_id = j["person"]["id"]
            player_number = int(j["jerseyNumber"])
            player_shifts = parse_shifts(id, home_team.id, player_id, player_number, home_shifts_html)
            home_shifts.extend(player_shifts)

    away_shifts = List()
    away_shifts_html = _fetch_shifts(id, "away")
    for j in json["liveData"]["boxscore"]["teams"]["away"]["players"].values():
        if j["person"]["id"] not in json["liveData"]["boxscore"]["teams"]["away"]["scratches"]:
            player_id = j["person"]["id"]
            player_number = int(j["jerseyNumber"])
            player_shifts = parse_shifts(id, away_team.id, player_id, player_number, away_shifts_html)
            away_shifts.extend(player_shifts)

    # all_events = List()
    # flip_sides = json["liveData"]["linescore"]["periods"][0]["home"]["rinkSide"] == "left"
    # for j in json["liveData"]["plays"]["allPlays"]:
    #     current_home_score = all_events.filter("type", "GOAL").filter("by_team.id", home_team.id).len
    #     current_away_score = all_events.filter("type", "GOAL").filter("by_team.id", away_team.id).len
    #     events = parse_eventss(info, current_home_score, current_away_score, home_shifts, away_shifts, j, flip_sides)
    #     all_events.extend(events)

    # TODO: Find a way to estimate this if not provided
    flip_sides = json["liveData"]["linescore"]["periods"][0]["home"].get("rinkSide", "right") == "left"

    events = List()
    for play in json["liveData"]["plays"]["allPlays"]:
        current_home_score = events.filter("type", "GOAL").filter("by_team.id", home_team.id).len
        current_away_score = events.filter("type", "GOAL").filter("by_team.id", away_team.id).len
        e = parse_events(play, info, current_home_score, current_away_score, home_shifts, away_shifts, flip_sides)
        events.extend(e)

    shifts = home_shifts + away_shifts
    player_stats = List()
    for player in players:
        ps = PlayerStats(player, shifts.filter("player_id", player.id), events.filter("by_player.id", player.id))
        player_stats.append(ps)

    return Game(info, home_team, away_team, player_stats, events)


def parse_location(json, gametime, flip_sides):
    if "x" in json:
        x = int(json["x"])
        y = int(json["y"])
        if flip_sides:
            x *= -1
            y *= -1
        if gametime.period % 2 == 0:
            x *= -1
            y *= -1
        return Location(x, y)
    else:
        return None


def parse_official(json):
    id = json["id"]
    if Official.has_key(id): return Official.from_key(id)
    name = json["fullName"]
    return Official(id, name)


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


def parse_shifts(game_id, team_id, player_id, player_number, html):
    shifts = List()
    tree = BeautifulSoup(html, features="html.parser")
    for row in tree.find_all("td",  "playerHeading + border"):
        number = int(row.get_text().split(" ")[0])
        if number != player_number:
            continue
        row = row.find_next("tr")
        while True:
            row = row.find_next("tr")
            cells = row.find_all("td")
            if len(cells) == 6:
                game_id = game_id
                team = Team.from_key(team_id)
                player = Player.from_key(player_id)
                shift_id = int(cells[0].get_text()) - 1
                period = int(cells[1].get_text())
                on_period_mmss = cells[2].get_text().split(" /")[0]
                off_period_mmss = cells[3].get_text().split(" /")[0]
                on = Gametime(period, _parse_gametime(on_period_mmss))
                off = Gametime(period, _parse_gametime(off_period_mmss))
                shift = Shift(game_id, player_id, shift_id, on, off)
                shifts.append(shift)
            else:
                break
    return shifts


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
    return List([parse_team(j) for j in json])


def parse_venue(json):
    id = json["id"]
    if Venue.has_key(id): return Venue.from_key(id)
    name = json["name"]
    return Venue(id, name)
