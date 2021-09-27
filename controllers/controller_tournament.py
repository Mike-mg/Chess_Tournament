#! /usr/bin/env python3
# coding:utf-8

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
        self.bdd = bdd.db_functions

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

    def show_tournament(self):
        """
        Displays the general information of the tournament
        """
        self.view_tournament.show_tournament(bdd.deserialize_table_tournament())

    def result_round(self):
        """
        Changes the points of the players at the end of each round
        """

        self.view_tournament.menu_tournament(ControllerTournament.TOURNAMENTS)

        result_round = self.view_tournament.result_round(
            ControllerTournament.TOURNAMENTS
        )

        tournament = ControllerTournament.TOURNAMENTS[result_round[0]]
        tournament.tours[result_round[1]][result_round[2]] = result_round[3]

        tournament.next_round()

    def save_tournament(self):
        self.bdd.serialize_tournament(ControllerTournament.TOURNAMENTS)
