#! /usr/bin/env python3
# coding:utf-8

from tinydb import TinyDB

import models

DB_PLAYERS = TinyDB('bdd/db_players.json', indent=4)
TABLE_PLAYERS = DB_PLAYERS.table("players")


def deserialized_table_players() -> list:
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


def serialized_player(list_players_object: list):
    """
    serialize the list of player objects in parameter
    """

    serialized_players_for_table_players = list()

    for player in list_players_object:

        player_serialized = dict()

        player_serialized['last_name'] = player.last_name
        player_serialized['name'] = player.name
        player_serialized['birthday'] = player.birthday
        player_serialized['sex'] = player.sex
        player_serialized['ranking'] = player.ranking
        player_serialized['points'] = player.points

        serialized_players_for_table_players.append(player_serialized)

    TABLE_PLAYERS.truncate()
    TABLE_PLAYERS.insert_multiple(serialized_players_for_table_players)


if __name__ == "__main__":
    pass
