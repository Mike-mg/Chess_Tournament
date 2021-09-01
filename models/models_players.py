#! /usr/bin/env python3
# coding:utf-8


from tinydb import TinyDB

db_players = TinyDB('Bdd/db_players.json', indent=4)
table_players = db_players.table("players")


class Player:
    """
    Class that creates player objects
    """

    def __init__(self, last_name: str, name: str, birthday: str, sex: str, ranking: int, points: int = 0):
        """
        Builds the player object
        """
        self.last_name = last_name.capitalize()
        self.name = name.capitalize()
        self.birthday = birthday
        self.sex = sex.capitalize()
        self.ranking = ranking
        self.point = points

    def deserialized_table_players(self, table_list_players=table_players):
        """
        Deserialized table players
        """

        all_players = list()

        for player in table_list_players:
            all_players.append(player)

        return all_players


def serialized_player(player):

    serial_player = dict()

    serial_player['last_name'] = player[0]
    serial_player['name'] = player[1]
    serial_player['birthday'] = player[2]
    serial_player['sex'] = player[3]
    serial_player['ranking'] = player[4]
    serial_player['points'] = player[5]

    table_players.insert(serial_player)


if __name__ == "__main__":
    pass
