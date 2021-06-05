#! /usr/bin/env python3
# coding:utf-8

from tinydb import TinyDB

import views.view_players
import models.models_players

DB_TOURNAMENTS = TinyDB('Bdd/db_tournaments.json', indent=4)
TOURNAMENTS = DB_TOURNAMENTS.table("tournaments")


class Tournament:
    """
    create a object Tournament
    """

    def __init__(self, name, location, start_date, end_date, nb_rounds,
                 tours, players, time_control, description):

        self.name = name.title()
        self.location = location.title()
        self.start_date = start_date
        self.end_date = end_date
        self.nb_rounds = nb_rounds
        self.tours = tours
        self.players = players
        self.time_control = time_control
        self.description = description

    def match(self):

        for k, v in enumerate(models.models_players.deserialized_table_players()):
            print(k, v)

        for i in self.players:
            print(i)
