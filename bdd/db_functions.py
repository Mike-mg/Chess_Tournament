#! /usr/bin/env python3
# coding:utf-8

from tinydb import TinyDB

import models

DB_PLAYERS = TinyDB("bdd/db_players.json", indent=4)
TABLE_PLAYERS = DB_PLAYERS.table("players")

DB_TOURNAMENTS = TinyDB("bdd/db_tournaments.json", indent=4)
TABLE_TOURNAMENTS = DB_TOURNAMENTS.table("tournaments")


def deserialize_table_players(table_player=TABLE_PLAYERS) -> list[models.Player]:
    """
    Deserialized object players in var all_players
    """

    all_players = []

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


def serialize_player(list_players_object: list[models.Player]):
    """
    serialize the list of player objects in parameter
    """

    serialized_players_for_table_players = []

    for player in list_players_object:
        player_serialized = {}

        player_serialized["last_name"] = player.last_name
        player_serialized["name"] = player.name
        player_serialized["birthday"] = player.birthday
        player_serialized["sex"] = player.sex
        player_serialized["ranking"] = player.ranking
        player_serialized["points"] = player.points

        serialized_players_for_table_players.append(player_serialized)

    TABLE_PLAYERS.truncate()
    TABLE_PLAYERS.insert_multiple(serialized_players_for_table_players)


def deserialize_table_tournaments(
    table_tournaments=TABLE_TOURNAMENTS,
) -> list[models.Tournament]:
    """
    Deserialized object tournament in var all_tournaments
    """

    all_tournaments = []

    for tournament in table_tournaments.all():

        players = []

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


def serialize_tournament(list_tournament_object: list):
    """
    serialize the list of tournament objects in parameter
    """

    TABLE_TOURNAMENTS.truncate()

    tournament_serialized_for_table_tournaments = []

    for tournament in list_tournament_object:

        players_ids = []
        tournament_serialized = {}

        for player in tournament.players:
            players_ids.append(player.player_id)

        tournament_serialized["name"] = tournament.name
        tournament_serialized["location"] = tournament.location
        tournament_serialized["start_date"] = tournament.start_date
        tournament_serialized["end_date"] = tournament.end_date
        tournament_serialized["players"] = players_ids
        tournament_serialized["time_control"] = tournament.time_control
        tournament_serialized["description"] = tournament.description
        tournament_serialized["nb_rounds"] = tournament.nb_rounds
        tournament_serialized["tours"] = tournament.tours

        tournament_serialized_for_table_tournaments.append(tournament_serialized)

    TABLE_TOURNAMENTS.insert_multiple(tournament_serialized_for_table_tournaments)


if __name__ == "__main__":
    pass
