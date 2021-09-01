#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
"""

import views.view_menu
import utility_functions.utils_func
import models.models_players



class ViewPlayer:

    def __init__(self):

        self.view_menu = views.view_menu.ViewMenu()

    def view_show_player(self, table_players=models.models_players.table_players.all()):
        """
        View show all player
        """

        all_players = table_players

        self.view_menu.show_menu()
        self.view_menu.sub_menu('* List of all players *')

        print(f"{'ID'.center(10)} | "
              f"{'Last name'.center(20)} | "
              f"{'Name'.center(20)} | "
              f"{'Birthday'.center(15)} | "
              f"{'Sex'.center(10)} | "
              f"{'Ranking'.center(10)} | "
              f"{'Points'.center(10)}"
              f"\n{'°' * 119}")

        for key, player in enumerate(all_players):

            print(f"{str(key).center(10)} | "
                  f"{player['Last_name'].center(20)} | "
                  f"{player['Name'].center(20)} | "
                  f"{player['Birthday'].center(15)} | "
                  f"{player['Sex'].center(10)} | "
                  f"{str(player['Ranking']).center(10)} | "
                  f"{str(player['Points']).center(10)}"
                  f"\n{'-' * 119}")

    def add_player(self):
        """
        Docstrings
        """

        self.view_menu.show_menu()
        self.view_menu.sub_menu("* Add A Player *")

        last_name = utility_functions.utils_func.format_string("Last name")
        name = utility_functions.utils_func.format_string("Name")
        birthday = utility_functions.utils_func.format_string("Birthday")
        sex = utility_functions.utils_func.format_string("Sex")
        ranking = utility_functions.utils_func.format_string("Ranking")
        points = 0

        return last_name, name, birthday, sex, ranking, points

    def new_player_ranking(self, players):

        self.view_show_player()

        select_player = int(input(f"\n{'-' * 41}\n{':: Select the player to be modified > '}"))

        for key, value in enumerate(players):

            if key == select_player:
                print(f"\n{'Select player :'} {value['Last_name']} {value['Name']}\n{'-' * 30}")

                new_ranking = int(input('Enter the new ranking : '))

                value['Ranking'] = new_ranking

                return key + 1, value

if __name__ == "__main__":
    pass