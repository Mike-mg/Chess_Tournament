#! /usr/bin/env python3
# coding:utf-8

import models
import views
import bdd


class ControllerPlayer:
    """
    Controls the user input for the player model
    """

    ALL_PLAYERS = bdd.deserialized_table_players()

    def __init__(self):

        self.view_player = views.ViewPlayer()

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

        new_player = models.Player(get_view_player[0],
                                   get_view_player[1],
                                   get_view_player[2],
                                   get_view_player[3],
                                   get_view_player[4])

        ControllerPlayer.ALL_PLAYERS.append(new_player)
        bdd.serialized_player(ControllerPlayer.ALL_PLAYERS)


    def modified_ranking(self):
        """
        Changes the player rank
        """

        self.view_player.new_player_ranking(ControllerPlayer.ALL_PLAYERS)
        bdd.serialized_player(ControllerPlayer.ALL_PLAYERS)