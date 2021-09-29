#! /usr/bin/env python3
# coding:utf-8

from tinydb import Query

import views
import models
import bdd


class ControllerTournament:
    """
    Controls the creation of tournaments
    """

    def __init__(self):
        self.view_tournament = views.ViewTournament()
        self.view_player = views.ViewPlayer()
        self.tournaments = bdd.deserialize_table_tournaments()
        self.players = bdd.deserialize_table_players()

    def controller_add_tournament(self):
        """
        Instance a tournament
        """

        main_info_tournament = self.view_tournament.main_tournament_info()
        add_player = self.view_tournament.add_player_tournament()

        tournament = models.models_tournaments.Tournament(
            main_info_tournament[0],
            main_info_tournament[1],
            main_info_tournament[2],
            main_info_tournament[3],
            add_player,
            main_info_tournament[4],
            main_info_tournament[5],
        )

        players_objets = []

        for player in tournament.players:

            player_dict = bdd.db_functions.TABLE_PLAYERS.get(doc_id=player)

            players_objets.append(
                models.Player(
                    player_dict["last_name"],
                    player_dict["name"],
                    player_dict["birthday"],
                    player_dict["sex"],
                    player_dict["ranking"],
                    player_dict["points"],
                    player
                )
            )

            tournament.players = players_objets

        self.tournaments.append(tournament)
        tournament.round_1()

    def show_tournament(self):
        """
        Displays the general information of the tournament
        """
        return self.players

        # self.view_tournament.show_tournament(self.tournaments)

    def result_round(self):
        """
        Changes the points of the players at the end of each round
        """

        tournament_query = Query()

        self.view_tournament.menu_tournament(self.tournaments)

        result_round = self.view_tournament.result_round(self.tournaments)

        tournament = self.tournaments[result_round[0]]

        tournament.tours[result_round[1]][result_round[2]] = result_round[3]

        tournament.next_round()

        bdd.db_functions.TABLE_TOURNAMENTS.update(
            {"tours": tournament.tours},
            tournament_query.name == tournament.name,
        )

    def save_tournaments(self, list_tournaments: list[models.Tournament]):
        """
        serialize all tournaments
        """

        bdd.serialize_tournament(list_tournaments)

    def players(self):
        print("ok")
