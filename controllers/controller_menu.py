#! /usr/bin/env python3
# coding:utf-8
import bdd
import controllers
import utils
import views


class ControllerMenu:
    """
    Controls the menu options selected by the user
    """

    def __init__(self):
        self.controller_tournament = controllers.ControllerTournament()
        self.controller_player = controllers.ControllerPlayer()
        self.view_menu = views.ViewMenu()
        self.view_tournament = views.ViewTournament()

    def show_menu(self) -> None:
        """
        Show the program menu
        """

        self.view_menu.show_menu()

    def choice_user_menu(self) -> bool:
        """
        Menu selection
        """

        choice = self.view_menu.choice_menu()

        if choice == 0:
            # Show all player
            self.controller_player.controller_show_player()

        elif choice == 1:
            # Add a player
            self.controller_player.controller_add_player()

        elif choice == 2:
            # Modified ranking player
            self.controller_player.modified_ranking()

        elif choice == 3:
            # Add a tournament
            self.controller_tournament.controller_add_tournament()

        elif choice == 4:
            # Modified a tournament
            self.controller_tournament.result_round()

        elif choice == 5:
            # List of all actors in alphabetical order
            self.view_tournament.show_all_players_alphabetical(bdd.deserialize_table_players())

        elif choice == 6:
            # List of all players in order of ranking
            self.view_tournament.show_all_players_ranking(bdd.deserialize_table_players())

        elif choice == 7:
            # List of all players in a tournament by ranking order
            self.view_tournament.show_all_players_ranking_by_tournament(bdd.deserialize_table_tournaments())

        elif choice == 8:
            # List of all players in a tournament in alphabetical order
            self.view_tournament.show_all_players_alphabetical_by_tournament(bdd.deserialize_table_tournaments())

        elif choice == 9:
            # List of all tournaments
            self.view_tournament.show_all_tournaments(bdd.deserialize_table_tournaments())

        elif choice == 10:
            # List of all rounds in a tournament
            self.view_tournament.show_all_rounds_by_tournaments(bdd.deserialize_table_tournaments())

        elif choice == 11:
            # List of all games in a tournament
            self.view_tournament.show_all_match_by_tournaments(bdd.deserialize_table_tournaments())

        elif choice == 12:
            # Generate flake8.html
            utils.report_flake8_html()

        elif choice == 13:
            # show menu
            self.show_menu()

        elif choice == 14:
            # Leave program
            self.controller_tournament.save_tournaments()
            return False
