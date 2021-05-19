#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
Modules Models
"""

import views.view_tournament
import models.models_tournaments


class ControllerAddTournament:

    """
    Class ControllerAddPlayer
    """

    @staticmethod
    def controller_add_tournament():
        """
        Add player control
        """

        tournament = views.view_tournament.ViewTournament.add_tournament()
        models.models_tournaments.Tournament(tournament["Name"],
                                 tournament["Location"],
                                 tournament["Start date"],
                                 tournament["End date"],
                                 tournament['Players'],
                                 tournament["Nb_rounds"],
                                 tournament["Tours"])

    @staticmethod
    def show_tournament():
        views.view_tournament.ViewTournament.show_all_tournament()

    @staticmethod
    def modified_tournament():
        views.view_tournament.ViewTournament.point_round_1()
