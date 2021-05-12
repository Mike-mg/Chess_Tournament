#! /usr/bin/env python3
# coding:utf-8

from tinydb import TinyDB


DB_PLAYERS = TinyDB('Bdd/db_players.json', indent=4)
DB_ALL_PLAYERS = DB_PLAYERS.table('players')

DB_TOURNAMENTS = TinyDB('Bdd/db_tournaments.json', indent=4)
DB_ALL_TOURNAMENTS = DB_TOURNAMENTS.table('tournaments')


class Player:

    """Docstring"""

    def __init__(self, last_name, name, birthday, sex, ranking, nb_rounds):

        player = {}

        self.last_name = last_name.capitalize()
        self.name = name.capitalize()
        self.birthday = birthday
        self.sex = sex.capitalize()
        self.ranking = ranking
        self.nb_rounds = nb_rounds

        player['Last name'] = self.last_name
        player['Name'] = self.name
        player['Birthday'] = self.birthday
        player['Sex'] = self.sex
        player['Ranking'] = self.ranking

        DB_ALL_PLAYERS.insert(player)


class Tournament:

    """Docstring"""

    def __init__(self, name, location, start_date, end_date, players, nb_rounds):

        tournament = {}

        self.name = name.title()
        self.location = location.title()
        self.start_date = start_date
        self.end_date = end_date
        self.nb_rounds = nb_rounds
        self.players = players

        tournament['Name'] = self.name
        tournament['Location'] = self.location
        tournament['Start date'] = self.start_date
        tournament['End date'] = self.end_date
        tournament['Players'] = self.players
        tournament['Nb_rounds'] = self.nb_rounds

        DB_ALL_TOURNAMENTS.insert(tournament)
