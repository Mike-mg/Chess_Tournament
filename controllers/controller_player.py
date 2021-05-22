#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
Modules Models
"""

import views.view_players
import models.models_players


class ControllerShowPlayers:
    """
        Class for the control show players
    """

    def __init__(self):
        """
        Shows all players
        """

        table_all_players = views.view_players.ViewShowPlayer(models.models_players.table_players.all())
        table_all_players.show_players()


class ControllerAddPlayer:
    """
    Class for the control add player
    """

    def __init__(self):
        """
        Add player control
        """

        add_player = views.view_players.ViewAddPlayer()

        player = models.models_players.Player(add_player.last_name,
                                              add_player.name,
                                              add_player.birthday,
                                              add_player.sex,
                                              add_player.ranking)

        player.serialized_player()


class ControllerRemovePlayer:
    """
        Class for the control remove player
    """

    def __init__(self):

        id_int = views.view_players.ViewRemovePlayer()
        id_int.remove_player()

        id_player = models.models_players.Remove(id_int.id_player_remove)
        id_player.remove()


class ControllerRankingPlayer:
    """
        Class for the new ranking player
    """

    def __init__(self):

        ranking = views.view_players.ViewRankingPlayer()
        ranking.new_ranking()

        new_ranking_player = models.models_players.NewRanking(ranking.player_id, ranking.ranking)
        new_ranking_player.new_ranking()
