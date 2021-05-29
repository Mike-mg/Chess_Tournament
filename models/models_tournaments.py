#! /usr/bin/env python3
# coding:utf-8

from tinydb import TinyDB

DB_TOURNAMENTS = TinyDB('Bdd/db_tournaments.json', indent=4)
TOURNAMENTS = DB_TOURNAMENTS.table("tournaments")


class Tournament:

    """
    create a object Tournament
    """

    def __init__(self,
                 name,
                 location,
                 start_date,
                 end_date,
                 nb_rounds,
                 tours,
                 players,
                 time_control,
                 description
                 ):

        tournament = {}

        self.name = name.title()
        self.location = location.title()
        self.start_date = start_date
        self.end_date = end_date
        self.nb_rounds = nb_rounds
        self.tours = tours
        self.players = players
        self.time_control = time_control
        self.description = description

        tournament['Name'] = self.name
        tournament['Location'] = self.location
        tournament['Start date'] = self.start_date
        tournament['End date'] = self.end_date
        tournament['Nb_rounds'] = self.nb_rounds
        tournament['Tours'] = self.tours
        tournament['Players'] = self.players
        tournament['Time_control'] = self.time_control
        tournament['Description'] = self.description

        TOURNAMENTS.insert(tournament)
