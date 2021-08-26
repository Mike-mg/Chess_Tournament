#! /usr/bin/env python3
# coding:utf-8

import controllers.controller_tournament
import controllers.controller_player
import views.view_menu


class ControllerMenu:

    def __init__(self):
        self.controller_tournament = controllers.controller_tournament.ControllerTournament()
        self.controller_player = controllers.controller_player.ControllerPlayer()
        self.view_menu = views.view_menu.ViewMenu()

    def show_menu(self):

        self.view_menu.show_menu()

    def choice_user_menu(self):

        choice = self.view_menu.choice_menu()

        if choice == 0:
            # Show all player
            self.controller_player.controller_show_player()

        elif choice == 1:
            # Add a player
            self.controller_player.controller_add_player()

        elif choice == 2:
            # Modified ranking player
            pass

        elif choice == 3:
            # List tournament
            self.controller_tournament.show_tournament()

        elif choice == 4:
            # Add a tournament
            self.controller_tournament.controller_add_tournament()

        elif choice == 5:
            # Modified a tournament
            self.controller_tournament.result_round()

        elif choice == 6:
            # show menu
            self.show_menu()

        elif choice == 7:
            # Leave program
            return False
