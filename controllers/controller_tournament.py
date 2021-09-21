#! /usr/bin/env python3
# coding:utf-8
import controllers
import views
import models
import bdd


class ControllerTournament:
    """
    Controls the creation of tournaments
    """
    # BDD_TOURNAMENTS = bdd.deserialized_table_tournament()
    TOURNAMENTS = []

    BDD_PLAYERS = bdd.deserialized_table_players()
    BDD_TOURNAMENTS = bdd.deserialized_table_tournament()

    def __init__(self):
        self.view_tournament = views.ViewTournament()
        self.view_player = views.ViewPlayer()

    def controller_add_tournament(self):
        """
        Instance a tournament
        """

        main_info_tournament = self.view_tournament.main_tournament_info()
        add_player = self.view_tournament.add_player_tournament()

        tournament = models.models_tournaments.Tournament(main_info_tournament[0],
                                                          main_info_tournament[1],
                                                          main_info_tournament[2],
                                                          main_info_tournament[3],
                                                          add_player,
                                                          main_info_tournament[4],
                                                          main_info_tournament[5])

        tournament.round_1()
        ControllerTournament.TOURNAMENTS.append(tournament)
        bdd.serialized_tournament(ControllerTournament.TOURNAMENTS)

    def show_tournament(self):
        """
        Displays the general information of the tournament
        """
        self.view_tournament.show_tournament(ControllerTournament.BDD_TOURNAMENTS)

    def result_round(self):
        """
        Changes the points of the players at the end of each round
        """

        self.view_tournament.menu_tournament(ControllerTournament.TOURNAMENTS)

        num_tournament, result_round_actual = self.view_tournament.result_round(ControllerTournament.TOURNAMENTS)

        tournament = ControllerTournament.TOURNAMENTS[num_tournament]

        tournament.next_round()
        bdd.serialized_tournament(ControllerTournament.TOURNAMENTS)
