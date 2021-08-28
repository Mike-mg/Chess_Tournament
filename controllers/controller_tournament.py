#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
Modules Models
"""

import views.view_tournament
import views.view_players
import views.view_menu
import models.models_tournaments


class ControllerTournament:
    """
    Controller tournament
    """
    tournaments = []

    def __init__(self):

        self.view_tournament = views.view_tournament.ViewTournament()

    def controller_add_tournament(self):

        # main_info_tournament = self.view_tournament.main_tournament_info()
        # add_player = self.view_tournament.add_player_tournament()

        # tournament = models.models_tournaments.Tournament(main_info_tournament[0],
        #                                                   main_info_tournament[1],
        #                                                   main_info_tournament[2],
        #                                                   main_info_tournament[3],
        #                                                   add_player,
        #                                                   main_info_tournament[4],
        #                                                   main_info_tournament[5])

        tournament = models.models_tournaments.Tournament("Tournament French",
                                                          "French",
                                                          "01/01/2020",
                                                          "01/01/2020",
                                                          [1, 2, 3, 4, 5, 6, 7, 8],
                                                          "time control",
                                                          "description")

        tournament.tours.insert(0, tournament.round_1())
        ControllerTournament.tournaments.append(tournament)

    def show_tournament(self):

        self.view_tournament.show_tournament(ControllerTournament.tournaments)

    def result_round(self):

        self.view_tournament.menu_tournament(ControllerTournament.tournaments)

        key_tournament, results_round = self.view_tournament.result_round(ControllerTournament.tournaments)

        tournament = ControllerTournament.tournaments[key_tournament]

        tournament.tours.insert(tournament.round_indicator, tournament.next_round(results_round))

        print("\n\n", tournament.tours[0])
