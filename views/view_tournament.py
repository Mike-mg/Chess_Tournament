#! /usr/bin/env python3
# coding:utf-8

"""
import views
"""

import datetime

import views.view_players
import views.view_menu
import models.models_players


def format_string(get_string):
    return input(f":: {get_string} > ")


class ViewAddTournament:
    """
    Objet tournament
    """

    def __init__(self):

        views.view_menu.show_menu()
        views.view_menu.sub_menu('* Add A Tournament *')

        self.name = str("chess 1")
        self.location = str("Boston")
        self.start_date = str("1/1/2020")
        self.end_date = str("1/1/2020")
        self.nb_rounds = int(2)
        self.tours = list()
        self.players = [1, 2]
        self.time_control = str("Bullet")
        self.description = str("Tournament of Boston")

    def name_tournament(self):
        """
        Name of tournament
        """

        self.name = format_string("Name tournament").title()

    def location_tournament(self):
        """
        Location of tournament
        """

        self.location = format_string("Location").title()

    def date_tournament(self):
        """
        start and end of tournament
        """

        try:
            print(f"\n{'Enter start date'}\n"
                  f"{'-' * 16}")

            year = int(format_string("Year"))
            month = int(format_string("Month"))
            day = int(format_string("Day"))
            start_date = datetime.date(year, month, day).strftime("%d/%m/%Y")

            print(f"\n{'Enter end date'}\n"
                  f"{'-' * 14}")
            year = int(format_string("Year"))
            month = int(format_string("Month"))
            day = int(format_string("Day"))
            end_date = datetime.date(year, month, day).strftime("%d/%m/%Y")

            self.start_date = start_date
            self.end_date = end_date

        except ValueError:
            print(f"\n{':: ERROR > Enter a valid date of birth like this'}\n"
                  f"{'-' * 48}\n"
                  f"{'Year : 1979'}\n"
                  f"{'Month : 07'}\n"
                  f"{'Day : 13'}\n")

    def nb_rounds_tournament(self):
        """
        Number de round of tournament
        """
        print()
        nb_rounds = int(format_string(f"NB rounds ( default '4' )"))

        try:

            if nb_rounds is False:
                nb_rounds = 4

            nb_rounds = int(nb_rounds)

        except ValueError:
            print(f"\n{':: ERROR > Enter a valid format, the rank must be a positive number'}\n")

        self.nb_rounds = nb_rounds

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
        nb_players = int(format_string("Number of players of tournament"))

        views.view_players.view_show_player(models.models_players.table_players.all())

        print(f"\n{'Select players by their index to add them to the tournament'}\n"
              f"{'-' * 59}")

        for i in range(nb_players):
            player = int(format_string(f"Player {i + 1} : "))
            self.players.append(player)

    def time_control_tournament(self):
        """
        Time control of tournament
        """

        list_time_control = ["Blitz", "Bullet", "Quick hit"]

        print()
        print(f"Select time control\n"
              f"{'-' * 19}")
        for key, time_control in enumerate(list_time_control):
            print(f"[ {key} ]  {time_control}")

        choice_time_control = int(format_string("Choice time control"))

        self.time_control = list_time_control[choice_time_control]

    def description_tournament(self):
        """
        Description of tournament
        """
        self.description = format_string("Description").title()

    def round_1_tournament(self, round_1):
        """
        Match tournament
        """

        self.tours[0] =  [tuple(round_1)]

    def results_round_1(self):
        """
        Results match round 1
        """
        result_player = tuple()

        print(f"\nResults Round 1\n"
              f"{'-' * 14}")

        for round in self.tours[0][0]:

            for key, value in round.items():

                dict_results = dict()
                new_score = float(format_string(f"""Player '{key}' New score : """))
                value = new_score
                dict_results[key] = value
                result_player += dict_results,

        self.tours[0] = [result_player]

    def round_2_tournament(self, round_2):
        """
        Match tournament
        """

        self.tours[1] = [tuple(round_2)]

    def results_round_2(self):
        """
        Results match round 2
        """
        result_player = tuple()

        print(f"\nResults Round 2\n"
              f"{'-' * 14}")

        for round in self.tours[1][0]:

            for key, value in round.items():

                dict_results = dict()
                new_score = float(format_string(f"""Player '{key}' New score : """))
                value = new_score
                dict_results[key] = value
                result_player += dict_results,

        self.tours[1] = [result_player]

if __name__ == "__main__":
    pass
