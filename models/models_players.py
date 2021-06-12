#! /usr/bin/env python3
# coding:utf-8


from tinydb import TinyDB

db_players = TinyDB('Bdd/db_players.json', indent=4)
table_players = db_players.table("players")


class Player:
    """
    Serialize and Create a object Player
    """

    def __init__(self, last_name, name, birthday, sex, ranking, points=0):

        self.last_name = last_name.capitalize()
        self.name = name.capitalize()
        self.birthday = birthday
        self.sex = sex.capitalize()
        self.ranking = ranking
        self.point = points


def serialized_player(player):

    serial_player = dict()

    serial_player['Last_name'] = player[0]
    serial_player['Name'] = player[1]
    serial_player['Birthday'] = player[2]
    serial_player['Sex'] = player[3]
    serial_player['Ranking'] = player[4]
    serial_player['Points'] = player[5]

    table_players.insert(serial_player)


def deserialized_table_players(table_list_players=table_players):
    """
    Deserialized table players
    """
    all_players = []

    for player in table_list_players:
        all_players.append(player)

    return all_players


if __name__ == "__main__":
    pass
