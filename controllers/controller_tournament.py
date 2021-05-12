#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
Modules Models
"""

import views.view_tournament
import models.models


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
        models.models.Tournament(tournament["Name"],
                                 tournament["Location"],
                                 tournament["Start date"],
                                 tournament["End date"],
                                 tournament['Players'],
                                 tournament["Nb_rounds"])
