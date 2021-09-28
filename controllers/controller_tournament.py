#! /usr/bin/env python3
# coding:utf-8

from tinydb import Query
import views
import models
import bdd


class ControllerTournament:
    """
    Controls the creation of tournaments
    """

    TOURNAMENTS = []

    def __init__(self):
        self.view_tournament = views.ViewTournament()
        self.view_player = views.ViewPlayer()

    def controller_add_tournament(self):
        """
        Instance a tournament
        """

        main_info_tournament = self.view_tournament.main_tournament_info()
        add_player = self.view_tournament.add_player_tournament()

        tournament = models.models_tournaments.Tournament(
            main_info_tournament[0],
            main_info_tournament[1],
            main_info_tournament[2],
            main_info_tournament[3],
            add_player,
            main_info_tournament[4],
            main_info_tournament[5],
        )

        ControllerTournament.TOURNAMENTS.append(tournament)
        tournament.round_1()
        bdd.serialize_tournament(ControllerTournament.TOURNAMENTS)

    def show_tournament(self):
        """
        Displays the general information of the tournament
        """

        self.view_tournament.show_tournament(bdd.deserialize_table_tournaments())

    def result_round(self):
        """
        Changes the points of the players at the end of each round
        """
        tournament_query = Query()

        self.view_tournament.menu_tournament(bdd.deserialize_table_tournaments())

        result_round = self.view_tournament.result_round(
            bdd.deserialize_table_tournaments()
        )

        for id_tournament, tournament in enumerate(bdd.deserialize_table_tournaments()):

            if id_tournament == result_round[0]:

                tournament.tours[result_round[1]][result_round[2]] = result_round[3]

                tournament.next_round()

                bdd.db_functions.TABLE_TOURNAMENTS.update({"tours":tournament.tours}, tournament_query.name == tournament.name)


