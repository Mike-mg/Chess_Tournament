#! /usr/bin/env python3
# coding:utf-8

from tinydb import Query

import views.view_players
import models.models_players
import views.view_menu


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

        get_view_player = self.view_player.add_player()
        models.models_players.serialized_player(get_view_player)

    def modified_ranking(self):

        update_ranking_player = Query()

        players = models.models_players.deserialized_table_players()

        update_player = self.view_player.new_player_ranking(players)

        models.models_players.table_players.update({'Ranking': update_player['Ranking']},
                                                   update_ranking_player.Name == update_player['Name'])

