#! /usr/bin/env python3
# coding:utf-8

import views.view_tournament
import views.view_menu
import controllers.controller_tournament
import controllers.controller_player


def choice_user_menu(choice):

    if choice == 0:
        # Show all player
        controllers.controller_player.controller_show_player()

    elif choice == 1:
        # Add a player
        controllers.controller_player.controller_add_player()

    elif choice == 2:
        # Modified ranking player
        pass

    elif choice == 3:
        pass

    elif choice == 4:
        # Add a tournament
        controllers.controller_tournament.controller_add_tournament()

    elif choice == 5:
        # Create a tournament
        views.view_tournament.ViewAddTournament.results_round_1()

    elif choice == 6:
        # Modified current tournament
        pass

    elif choice == 7:
        # show menu
        views.view_menu.show_menu()

    elif choice == 8:
        return False