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

    def serialized_player(self):

        player = dict()

        player['Last_name'] = self.last_name
        player['Name'] = self.name
        player['Birthday'] = self.birthday
        player['Sex'] = self.sex
        player['Ranking'] = self.ranking

        table_players.insert(player)


class Remove:
    """
    Remove Player
    """

    def __init__(self, player_id):

        self.player_id = player_id

    def remove(self):
        table_players.remove(doc_ids=[self.player_id])


class NewRanking:
    """
    Docstrings
    """

    def __init__(self, player_id, ranking):

        self.player_id = player_id
        self.ranking = ranking

    def new_ranking(self):
        table_players.update({'Ranking': self.ranking}, doc_ids=[self.player_id])


if __name__ == "__main__":
    pass
