#! /usr/bin/env python3
# coding:utf-8

import models.models_players
import views.view_menu
import views.view_players
import bdd.db_functions


class ControllerPlayer:
    """
    Controls the user input for the player model
    """

    ALL_PLAYERS = bdd.db_functions.deserialized_table_players()

    def __init__(self):

        self.view_player = views.view_players.ViewPlayer()

    def controller_show_player(self):
        """
        Shows all players
        """

        self.view_player.view_show_player()

    def controller_add_player(self):
        """
        Add player control
        """

        get_view_player = self.view_player.add_player()
        print(get_view_player)
        print(ControllerPlayer.ALL_PLAYERS)

        new_player = models.models_players.Player(get_view_player[0],
                                                  get_view_player[1],
                                                  get_view_player[2],
                                                  get_view_player[3],
                                                  get_view_player[4],
                                                  get_view_player[5])

        ControllerPlayer.ALL_PLAYERS.append(new_player)

    def modified_ranking(self):
        """
        Changes the player rank
        """

        self.view_player.new_player_ranking(ControllerPlayer.ALL_PLAYERS)
        bdd.db_functions.serialized_player(ControllerPlayer.ALL_PLAYERS)
