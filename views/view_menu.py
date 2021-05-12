#! /usr/bin/env python3
# coding:utf-8

import os
import sys

import views.view_tournament
import views.view_players
import controllers.controller_tournament
import controllers.controller_player


class ShowMenu:

    @staticmethod
    def menu():

        if sys.platform.startswith('linux'):
            os.system('clear')
        elif sys.platform.startswith('win32'):
            os.system('cls')
        elif sys.platform.startswith('darwin'):
            os.system('clear')

        menu_list = ['Add a player',
                     'List of all players',
                     'Create a tournament',
                     'Show all tournaments',
                     'Check current tournaments',
                     'Leave -*- CHESS TOURNAMENT -*-',
                     'Return menu']

        print(f"\n\n{'=' * 119}\n"
              f"{'|'}{'-*- CHESS TOURNAMENT -*-'.center(117)}{'|'}\n"
              f"{'=' * 119}\n\n")

        print(f"{'=' * 119}\n"
              f"{'|'}{'* MENU *'.center(117)}{'|'}\n"
              f"{'-' * 119}")

        for index, m_menu in enumerate(menu_list):
            print(f"{':: '}{index} > {m_menu}")

        print(f"{'-' * 119}")

    @staticmethod
    def choice_menu():

        while 1:

            choice = input(f"\n{'=' * 22}\n"
                           f"{'Help : 6 > Return menu'}"
                           f"\n{'-' * 22}"
                           f"\n{':: Select a option > '}")

            try:
                choice = int(choice)

            except ValueError:
                print(f"\n{':: ERROR > Enter a valid option'}\n")
                continue

            if choice == 0:
                # Add a player
                controllers.controller_player.ControllerAddPlayer.controller_add_player()

            elif choice == 1:
                # Show all player
                views.view_players.ViewPlayer.show_players()
            elif choice == 2:
                # Create a tournament
                controllers.controller_tournament.ControllerAddTournament.controller_add_tournament()

            elif choice == 3:
                # Show current tournament
                pass

            elif choice == 4:
                # Check current tournament
                pass

            elif choice == 6:
                # show menu
                ShowMenu.menu()

            elif choice in [7, 8, 9]:
                print(f"\n:: ERROR > Enter a valid option")

            else:
                break
