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


def controller_show_player():
    """
    Shows all players
    """

    views.view_players.view_show_player(models.models_players.table_players.all())


def controller_add_player():
    """
    Add player control
    """

    player = views.view_players.add_player()
    models.models_players.serialized_player(player)



    # list_players_tournament = list()
    #
    # for player in views.view_players.view_add_player():
    #     list_players_tournament.append(player)

# class ControllerRankingPlayer:
#     """
#         Class for the new ranking player
#     """
#
#     def __init__(self):
#
#         ranking = views.view_players.ViewRankingPlayer()
#         ranking.new_ranking()
#
#         new_ranking_player = models.models_players.new_rankin(ranking.player_id, ranking.ranking)
#         new_ranking_player.new_ranking()
