#! /usr/bin/env python3
# coding:utf-8

import views
import models


class ControllerTournament:
    """
    Controls the creation of tournaments
    """

    TOURNAMENTS = []

    def __init__(self):

        self.view_tournament = views.view_tournament.ViewTournament()
        self.view_player = views.view_players.ViewPlayer()

    def controller_add_tournament(self):
        """
        Instance a tournament
        """

        # main_info_tournament = self.view_tournament.main_tournament_info()
        # add_player = self.view_tournament.add_player_tournament()

        # tournament = models.models_tournaments.Tournament(main_info_tournament[0],
        #                                                   main_info_tournament[1],
        #                                                   main_info_tournament[2],
        #                                                   main_info_tournament[3],
        #                                                   add_player,
        #                                                   main_info_tournament[4],
        #                                                   main_info_tournament[5])

        tournament = models.models_tournaments.Tournament("Tournament 1",
                                                          "French",
                                                          "01/01/2020",
                                                          "01/01/2020",
                                                          [1, 2, 3, 4, 5, 6, 7, 8],
                                                          "time control",
                                                          "description")

        tournament.round_1()
        ControllerTournament.TOURNAMENTS.append(tournament)

    def show_tournament(self):
        """
        Displays the general information of the tournament
        """

        self.view_tournament.show_tournament(ControllerTournament.TOURNAMENTS)

    def result_round(self):
        """
        Changes the points of the players at the end of each round
        """

        self.view_tournament.menu_tournament(ControllerTournament.TOURNAMENTS)

        num_tournament, result_round_actual = self.view_tournament.result_round(ControllerTournament.TOURNAMENTS)

        tournament = ControllerTournament.TOURNAMENTS[num_tournament]
        tournament.next_round()
