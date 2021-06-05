#! /usr/bin/env python3
# coding:utf-8

"""
import views
"""

import datetime

import views.view_players
import views.view_menu


def format_string(get_string):
    return input(f":: {get_string} > ")


class ViewTournament:
    """
    Objet tournament
    """

    def __init__(self):

        # self.name = str()
        # self.location = str()
        # self.start_date = str()
        # self.end_date = str()
        # self.nb_rounds = 4
        # self.tours = list()
        # self.players = []
        # self.time_control = str()
        # self.description = str()

        self.name = str("chess 1")
        self.location = str("France")
        self.start_date = str("01/01/2021")
        self.end_date = str("01/01/2021")
        self.nb_rounds = 4
        self.tours = list()
        self.players = [1, 2, 3, 4, 5, 6, 7, 8]
        self.time_control = str("Bullet")
        self.description = str("Tournament of 01/01/2021 in France ")

    def main_tournament_info(self):
        """
        Name, location, date, description and time control of tournament
        """

        views.view_menu.show_menu()
        views.view_menu.sub_menu('* Add A Tournament *')

        self.name = format_string("Name tournament").capitalize()
        self.location = format_string("Location").capitalize()
        self.description = format_string("Description").capitalize()

        date_string = [f"\nEnter start date\n{'-' * 16}",
                       f"\nEnter end date\n{'-' * 14}"]

        date = []

        for i in range(2):

            print(date_string[i])

            year = int(format_string("Year"))
            month = int(format_string("Month"))
            day = int(format_string("Day"))
            date.append(datetime.date(year, month, day).strftime("%d/%m/%Y"))

        self.start_date = date[0]
        self.end_date = date[1]

        list_time_control = ["Blitz", "Bullet", "Quick hit"]

        print(f"\nSelect time control\n{'-' * 19}")

        for key, time_control in enumerate(list_time_control):
            print(f"[ {key} ]  {time_control}")

        choice_time_control = int(format_string("Choice time control"))

        self.time_control = list_time_control[choice_time_control]

    def tours_tournament(self):
        """
        Tours of tournament
        """
        for i in range(self.nb_rounds):
            self.tours.append([])

    def add_player_tournament(self):
        """
        Add player at a tournament
        """

        views.view_players.view_show_player()

        print(f"\n{'Select players by their index to add them to the tournament'}\n"
              f"{'-' * 59}")

        for i in range(8):
            player = int(format_string(f"Player {i + 1}"))
            self.players.append(player)

    def show_tournament(self, tournament):

        views.view_menu.sub_menu(f"Tournament {tournament.name}")

        print(f"{':: Name tournament':<20}{'> '}{tournament.name}\n"
              f"{':: Location':<20}{'> '}{tournament.location}\n"
              f"{':: Start date':<20}{'> '}{tournament.start_date}\n"
              f"{':: End date':<20}{'> '}{tournament.end_date}\n"
              f"{':: Nb rounds':<20}{'> '}{tournament.nb_rounds}\n"
              f"{':: Tours':<20}{'> '}{tournament.tours}\n"
              f"{':: Players':<20}{'> '}{tournament.players}\n"
              f"{':: Time control':<20}{'> '}{tournament.time_control}\n"
              f"{':: Description':<20}{'> '}{tournament.description}")


if __name__ == "__main__":
    pass
