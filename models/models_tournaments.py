#! /usr/bin/env python3
# coding:utf-8

from tinydb import TinyDB

DB_TOURNAMENTS = TinyDB('Bdd/db_tournaments.json', indent=4)
TOURNAMENTS = DB_TOURNAMENTS.table("tournaments")


class Tournament:

    """
    create a object Tournament
    """

    def __init__(self, name, location, start_date, end_date, players, nb_rounds, tours):

        tournament = {}

        self.name = name.title()
        self.location = location.title()
        self.start_date = start_date
        self.end_date = end_date
        self.nb_rounds = nb_rounds
        self.players = players
        self.tours = tours

        tournament['Name'] = self.name
        tournament['Location'] = self.location
        tournament['Start date'] = self.start_date
        tournament['End date'] = self.end_date
        tournament['Players'] = self.players
        tournament['Nb_rounds'] = self.nb_rounds
        tournament['Tours'] = self.tours

        TOURNAMENTS.insert(tournament)