#! /usr/bin/env python3
# coding:utf-8

import bdd
import models
import views


class ControllerPlayer:
    """
    Controls the user input for the player model
    """

    def __init__(self):

        self.view_player = views.ViewPlayer()
        self.players = bdd.deserialize_table_players()

    def controller_show_player(self):
        """
        Shows all players
        """

        self.view_player.view_show_player(self.players)

    def controller_add_player(self):
        """
        Add player control
        """

        get_view_player = self.view_player.add_player()

        new_player = models.Player(
            get_view_player[0],
            get_view_player[1],
            get_view_player[2],
            get_view_player[3],
            get_view_player[4],
        )

        self.players.append(new_player)
        bdd.serialize_player(self.players)

    def modified_ranking(self):
        """
        Changes the player rank
        """
        self.view_player.new_player_ranking(self.players)
        bdd.serialize_player(self.players)
