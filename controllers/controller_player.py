#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
Modules Models
"""

import views.view_players
import models.models


class ControllerAddPlayer:

    """
    Class ControllerAddPlayer
    """

    @staticmethod
    def controller_add_player():
        """
        Add player control
        """

        player = views.view_players.ViewPlayer.add()
        models.models.Player(player["last_name"],
                             player["name"],
                             player["birth_day"],
                             player["sex"],
                             player["ranking"])

    @staticmethod
    def controller_player_remove():
        views.view_players.ViewPlayer.remove()

    @staticmethod
    def controller_player_ranking():
        views.view_players.ViewPlayer.ranking()

