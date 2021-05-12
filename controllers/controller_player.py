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

        player = views.view_players.ViewPlayer.add_player()
        models.models.Player(player["last_name"],
                             player["name"],
                             player["birth_day"],
                             player["sex"],
                             player["ranking"])
