#! /usr/bin/env python3
# coding:utf-8


from tinydb import TinyDB

db_players = TinyDB('Bdd/db_players.json', indent=4)
table_players = db_players.table("players")


class Player:
    """
    Serialize and Create a object Player
    """

    def __init__(self, last_name, name, birthday, sex, ranking):

        self.last_name = last_name.capitalize()
        self.name = name.capitalize()
        self.birthday = birthday
        self.sex = sex.capitalize()
        self.ranking = ranking


def serialized_player(players):

    player = dict()

    players['Last_name'] = player['Last_name']
    players['Name'] = player['Ranking']
    players['Birthday'] = player['Ranking']
    players['Sex'] = player['Ranking']
    players['Ranking'] = player['Ranking']

    table_players.insert(player)


def deserialized_table_players(table_list_players):
    """
    Deserialized table players
    """
    all_players = []

    for player in table_list_players:

        player_dict = dict()

        player['Last_name'] = player_dict['Last_name']
        player['Name'] = player_dict['Ranking']
        player['Birthday'] = player_dict['Ranking']
        player['Sex'] = player_dict['Ranking']
        player['Ranking'] = player_dict['Ranking']

        all_players.append(player_dict)

    return all_players


if __name__ == "__main__":
    pass
