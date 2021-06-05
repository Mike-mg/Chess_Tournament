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

        # self.view_add_tournament.main_tournament_info()
        self.view_tournament.tours_tournament()
        # self.view_add_tournament.add_player_tournament()

        tournament = models.models_tournaments.Tournament(self.view_tournament.name,
                                                          self.view_tournament.location,
                                                          self.view_tournament.start_date,
                                                          self.view_tournament.end_date,
                                                          self.view_tournament.nb_rounds,
                                                          self.view_tournament.tours,
                                                          self.view_tournament.players,
                                                          self.view_tournament.time_control,
                                                          self.view_tournament.description)

        tournament.match()

        ControllerTournament.tournaments.append(tournament)
        # views.view_menu.show_menu()

    def show_tournament(self):

        views.view_menu.show_menu()

        for all_tournament in ControllerTournament.tournaments:
            self.view_tournament.show_tournament(all_tournament)
