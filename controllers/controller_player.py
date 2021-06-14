#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
Modules Models
"""

import views.view_players
import models.models_players
import views.view_menu


def format_string(get_string):
    return input(f":: {get_string} > ")


class ControllerPlayer:
    """
    Docstrings
    """

    def __init__(self):

        self.view_player = views.view_players.ViewPlayer()

    def controller_show_player(self):
        """
        Shows all players
        """

        self.view_player.view_show_player(models.models_players.table_players.all())


    def controller_add_player(self):
        """
        Add player control
        """
        player = self.view_player.add_player()
        models.models_players.serialized_player(player)
