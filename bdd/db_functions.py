#! /usr/bin/env python3
# coding:utf-8

from tinydb import TinyDB

import models

DB_PLAYERS = TinyDB("bdd/db_players.json", indent=4)
TABLE_PLAYERS = DB_PLAYERS.table("players")

DB_TOURNAMENTS = TinyDB("bdd/db_tournaments.json", indent=4)
TABLE_TOURNAMENTS = DB_TOURNAMENTS.table("tournaments")


def deserialized_table_players(table_player=TABLE_PLAYERS) -> list[models.Player]:
    """
    Deserialized object players in var all_players
    """

    all_players = list()

    for player in table_player.all():

        all_players.append(
            models.Player(
                player["last_name"],
                player["name"],
                player["birthday"],
                player["sex"],
                player["ranking"],
                player["points"],
                player.doc_id,
            )
        )

    return all_players


def serialized_player(list_players_object: list[models.Player]):
    """
    serialize the list of player objects in parameter
    """

    serialized_players_for_table_players = list()

    for player in list_players_object:
        player_serialized = dict()

        player_serialized["last_name"] = player.last_name
        player_serialized["name"] = player.name
        player_serialized["birthday"] = player.birthday
        player_serialized["sex"] = player.sex
        player_serialized["ranking"] = player.ranking
        player_serialized["points"] = player.points

        serialized_players_for_table_players.append(player_serialized)

    TABLE_PLAYERS.truncate()
    TABLE_PLAYERS.insert_multiple(serialized_players_for_table_players)


def deserialized_table_tournament() -> list:
    """
    Deserialized object tournament in var all_tournaments
    """

    all_tournaments = list()
    players = []

    for tournament in TABLE_TOURNAMENTS.all():

        for player in tournament["players"]:
            player_dict = TABLE_PLAYERS.get(doc_id=player)

            players.append(
                models.Player(
                    player_dict["last_name"],
                    player_dict["name"],
                    player_dict["birthday"],
                    player_dict["sex"],
                    player_dict["ranking"],
                    player_dict["points"],
                )
            )

        all_tournaments.append(
            models.Tournament(
                tournament["name"],
                tournament["location"],
                tournament["start_date"],
                tournament["end_date"],
                players,
                tournament["time_control"],
                tournament["description"],
                tournament["nb_rounds"],
                tournament["tours"],
            )
        )

    return all_tournaments


def serialized_tournament(list_tournament_object: list):
    """
    serialize the list of tournament objects in parameter
    """

    player_serialized = dict()
    player_serialized_for_table_tournaments = list()

    for tournament in list_tournament_object:

        player_serialized["name"] = tournament.name
        player_serialized["location"] = tournament.location
        player_serialized["start_date"] = tournament.start_date
        player_serialized["end_date"] = tournament.end_date
        player_serialized["players"] = tournament.players
        player_serialized["time_control"] = tournament.time_control
        player_serialized["description"] = tournament.description
        player_serialized["nb_rounds"] = tournament.nb_rounds
        player_serialized["tours"] = tournament.tours

        player_serialized_for_table_tournaments.append(player_serialized)

    TABLE_TOURNAMENTS.truncate()
    TABLE_TOURNAMENTS.insert_multiple(player_serialized_for_table_tournaments)


if __name__ == "__main__":
    pass
