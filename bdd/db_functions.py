#! /usr/bin/env python3
# coding:utf-8

from tinydb import TinyDB

import models

DB_PLAYERS = TinyDB('bdd/db_players.json', indent=4)
TABLE_PLAYERS = DB_PLAYERS.table("players")

DB_TOURNAMENTS = TinyDB('bdd/db_tournaments.json', indent=4)
TABLE_TOURNAMENTS = DB_TOURNAMENTS.table("tournaments")


def deserialized_table_players() -> list[models.Player]:
    """
    Deserialized object players in var all_players
    """

    all_players = list()

    for player in TABLE_PLAYERS.all():
        all_players.append(models.Player(player["last_name"],
                                         player["name"],
                                         player["birthday"],
                                         player["sex"],
                                         player["ranking"],
                                         player["points"]))

    return all_players


def serialized_player(list_players_object: list[models.Player]):
    """
    serialize the list of player objects in parameter
    """

    serialized_players_for_table_players = list()

    for player in list_players_object:
        tournament_serialized = dict()

        tournament_serialized['last_name'] = player.last_name
        tournament_serialized['name'] = player.name
        tournament_serialized['birthday'] = player.birthday
        tournament_serialized['sex'] = player.sex
        tournament_serialized['ranking'] = player.ranking
        tournament_serialized['points'] = player.points

        serialized_players_for_table_players.append(tournament_serialized)

    TABLE_PLAYERS.truncate()
    TABLE_PLAYERS.insert_multiple(serialized_players_for_table_players)


def deserialized_table_tournament() -> list:
    """
    Deserialized object tournament in var all_tournaments
    """

    all_tournaments = list()

    for tournament in TABLE_TOURNAMENTS.all():
        all_tournaments.append(models.Tournament(tournament['name'],
                                                 tournament['location'],
                                                 tournament['start_date'],
                                                 tournament['end_date'],
                                                 tournament['players'],
                                                 tournament['time_control'],
                                                 tournament['description'],
                                                 tournament['nb_rounds'],
                                                 tournament['tours']))

    return all_tournaments


def serialized_tournament(list_tournament_object: list):
    """
    serialize the list of tournament objects in parameter
    """

    tournament_serialized = dict()
    serialized_tournament_for_table_tournaments = list()

    for tournament in list_tournament_object:
        players = []
        for player in tournament.players:
            players.append([player.last_name,
                            player.name,
                            player.birthday,
                            player.sex,
                            player.ranking,
                            player.points])


        tournament_serialized['name'] = tournament.name
        tournament_serialized['location'] = tournament.location
        tournament_serialized['start_date'] = tournament.start_date
        tournament_serialized['end_date'] = tournament.end_date
        tournament_serialized['players'] = players
        tournament_serialized['time_control'] = tournament.time_control
        tournament_serialized['description'] = tournament.description
        tournament_serialized['nb_rounds'] = tournament.nb_rounds
        tournament_serialized['tours'] = tournament.tours

        serialized_tournament_for_table_tournaments.append(tournament_serialized)

    TABLE_TOURNAMENTS.truncate()
    TABLE_TOURNAMENTS.insert_multiple(serialized_tournament_for_table_tournaments)


if __name__ == "__main__":
    pass
