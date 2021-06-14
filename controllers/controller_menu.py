#! /usr/bin/env python3
# coding:utf-8

import controllers.controller_tournament
import controllers.controller_player


class ControllerMenu:

    def __init__(self):

        self.controller_player = controllers.controller_player.ControllerPlayer()

    def choice_user_menu(self, choice):

        if choice == 0:
            # Show all player
            self.controller_player.controller_show_player()

        elif choice == 1:
            # Add a player
            pass

        elif choice == 2:
            # Modified ranking player
            pass

        elif choice == 3:
            pass

        elif choice == 4:
            # Add a tournament
            pass

        elif choice == 5:
            # Show a tournament
            pass

        elif choice == 6:
            # Modified current tournament
            pass

        elif choice == 7:
            # show menu
            pass

        elif choice == 8:
            return False
