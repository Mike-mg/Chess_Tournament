#! /usr/bin/env python3
# coding:utf-8

from tinydb import TinyDB

DB_PLAYERS = TinyDB('Bdd/db_players.json', indent=4)
PLAYERS = DB_PLAYERS.table("players")


class SerializedPlayer:

    """
    Serialize and Create a object Player
    """

    def __init__(self, last_name, name, birthday, sex, ranking):

        player = {}

        self.last_name = last_name.capitalize()
        self.name = name.capitalize()
        self.birthday = birthday
        self.sex = sex.capitalize()
        self.ranking = ranking

        player['Last_name'] = self.last_name
        player['Name'] = self.name
        player['Birthday'] = self.birthday
        player['Sex'] = self.sex
        player['Ranking'] = self.ranking

        PLAYERS.insert(player)


class DeserializePlayer:

    """
        Deserialize a object Player
    """

    @staticmethod
    def players(db_players):

        players = []

        for all_players in db_players:
            player = dict()
            player['Last_name'] = all_players['Last_name']
            player['Name'] = all_players['Name']
            player['Birthday'] = all_players['Birthday']
            player['Sex'] = all_players['Sex']
            player['Ranking'] = all_players['Ranking']

            players.append(player)

        return players