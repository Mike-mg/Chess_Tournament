#! /usr/bin/env python3
# coding:utf-8

import views.view_players
import views.view_menu
import controllers.controller_tournament
import controllers.controller_player


class ChoiceMenu:

    @staticmethod
    def choice_user_menu(choice):

        if choice == 0:
            # Show all player
            views.view_players.ViewPlayer.show()

        elif choice == 1:
            # Add a player
            controllers.controller_player.ControllerAddPlayer.controller_add_player()

        elif choice == 2:
            # Modified ranking player
            controllers.controller_player.ControllerAddPlayer.controller_player_ranking()

        elif choice == 3:
            # Remove player
            controllers.controller_player.ControllerAddPlayer.controller_player_remove()

        elif choice == 4:
            # Show current tournament
            controllers.controller_tournament.ControllerAddTournament.show_tournament()

        elif choice == 5:
            # Create a tournament
            controllers.controller_tournament.ControllerAddTournament.controller_add_tournament()

        elif choice == 6:
            # Modified current tournament
            controllers.controller_tournament.ControllerAddTournament.modified_tournament()

        elif choice == 7:
            # show menu
            views.view_menu.ShowMenu.menu()

        elif choice == 8:
            return 0
