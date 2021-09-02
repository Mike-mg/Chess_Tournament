#! /usr/bin/env python3
# coding:utf-8

from tinydb import TinyDB

import models.models_players

db_players = TinyDB('db_players.json', indent=4)
table_players = db_players.table("players")


def deserialized_table_players(table_list_players: dict = table_players):
    """
    Deserialized object players in var all_players
    """
    print(table_list_players)

    all_players = list()

    for player in table_list_players:

        all_players.append(models.models_players.Player(player["last_name"],
                                                        player["name"],
                                                        player["birthday"],
                                                        player["sex"],
                                                        player["ranking"],
                                                        player["points"]))

    return all_players


def serialized_player(list_players: list):

    table_players.truncate()  # clear the table players
    serialized_players_for_table_players = list()

    for player in list_players:

        player_serialized = dict()

        player_serialized['last_name'] = player.last_name
        player_serialized['name'] = player.name
        player_serialized['birthday'] = player.birthday
        player_serialized['sex'] = player.sex
        player_serialized['ranking'] = player.ranking
        player_serialized['points'] = player.points

        serialized_players_for_table_players.append(player_serialized)

    table_players.insert_multiple(serialized_players_for_table_players)


if __name__ == "__main__":
    deserialized_table_players()
