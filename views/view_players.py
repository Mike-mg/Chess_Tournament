#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
"""

import datetime

import views.view_menu
import models.models_players


def format_string(get_string):
    return input(f":: {get_string} > ")


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

        last_name = format_string("Last name")
        name = format_string("Name")
        birthday = format_string("Birthday")
        sex = format_string("Sex")
        ranking = format_string("Ranking")
        points = 0

        return last_name, name, birthday, sex, ranking, points


if __name__ == "__main__":
    pass