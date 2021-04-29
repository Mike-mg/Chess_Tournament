#! usr/bin/env python3
# coding:utf-8

import models
import view


class BColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Menu:

    @classmethod
    def choice_menu(cls):

        while True:
            choice = input("\n# Select a option : ")

            try:
                choice = int(choice)

            except ValueError:
                print(f"\n:: {BColors.FAIL}{BColors.BOLD}ERROR{BColors.END} >"
                      f" {BColors.GREEN}Enter a valid option{BColors.END}")
                continue

            if choice == 0:
                # Add a player
                view.ShowMenu.menu()
                models.Player.add_player()

            elif choice == 1:
                # Show all player
                view.ShowMenu.menu()
                models.Player.show_players()

            elif choice == 2:
                # Create a tournament
                view.ShowMenu.menu()
                models.Tournament.create_tournament()

            elif choice == 3:
                # Show current tournament
                view.ShowMenu.menu()
                models.Tournament.show_tournament()

            elif choice == 4:
                # Check current tournament
                pass

            else:
                return False


if __name__ == "__main__":
    pass
