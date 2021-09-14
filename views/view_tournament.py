#! /usr/bin/env python3
# coding:utf-8

"""
import views
"""

import datetime

import views
import utils


class ViewTournament:
    """
    Show and retrieve tournament information
    """

    TIMES_CONTROL = ["Blitz", "Bullet", "Quick hit"]

    def __init__(self):

        self.menu = views.ViewMenu()
        self.view_player = views.ViewPlayer()

    def menu_tournament(self, list_tournament: list):
        """
        Show menu tournament
        """

        self.menu.sub_menu("Current tournament")

        for key, value in enumerate(list_tournament):
            print(f"[ {key} ] - [ {value.name}, {value.location} ]")

    def main_tournament_info(self) -> tuple:
        """
        Add a tournament
        Retrieve name, location, date, description and time control of tournament
        """

        self.menu.sub_menu('* Add A Tournament *')

        name = utils.format_string("Name tournament").capitalize()
        location = utils.format_string("Location").capitalize()
        description = utils.format_string("Description").capitalize()

        date_string = (f"\nEnter start date\n{'-' * 16}",
                       f"\nEnter end date\n{'-' * 14}")

        date = []

        for value in date_string:

            print(value)

            year = int(utils.format_string("Year"))
            month = int(utils.format_string("Month"))
            day = int(utils.format_string("Day"))
            date.append(datetime.date(year, month, day).strftime("%d/%m/%Y"))

        start_date = date[0]
        end_date = date[1]

        print(f"\nSelect time control\n{'-' * 19}")

        for key, time_control in enumerate(ViewTournament.TIMES_CONTROL):
            print(f"[ {key} ]  {time_control}")

        choice_time_control = int(utils.format_string("Choice time control"))

        time_control = ViewTournament.TIMES_CONTROL[choice_time_control]

        nb_rounds = int(utils.format_string("Number of rounds"))

        return name, location, start_date, end_date, time_control, description, nb_rounds

    def add_player_tournament(self) -> list:
        """
        Add player a tournament
        """

        self.view_player.view_show_player()

        print(f"\n{'Select players by their index to add them to the tournament'}\n"
              f"{'-' * 59}")

        players = []

        for i in range(8):

            player = int(utils.format_string(f"Player {i + 1}"))

            players.append(player)

        return players

    def show_tournament(self, list_tournament: list):
        """
        Show general tournament information
        """

        if len(list_tournament) == 0:
            print(f"\n{'-' * 38}\n"
                  f"*** It does not have a tournament ***\n"
                  f"{'-' * 38}")

        else:

            self.menu.show_menu()
            self.menu_tournament(list_tournament)

            select_tournament = int(input(f"\n{'-' * 37}\n{':: Select the tournament to be show > '}"))

            for key, tournament in enumerate(list_tournament):
                if key == select_tournament:

                    self.menu.sub_menu(f"{tournament.name} - {tournament.description}")

                    print(f"{':: Number tournament':<22}{'> '}{key}\n"
                          f"{':: Name tournament':<22}{'> '}{tournament.name}\n"
                          f"{':: Location':<22}{'> '}{tournament.location}\n"
                          f"{':: Start date':<22}{'> '}{tournament.start_date}\n"
                          f"{':: End date':<22}{'> '}{tournament.end_date}\n"
                          f"{':: Nb rounds':<22}{'> '}{tournament.nb_rounds}\n"
                          f"{':: Players':<22}{'> '}{tournament.players}\n"
                          f"{':: Time control':<22}{'> '}{tournament.time_control}\n"
                          f"{':: Description':<22}{'> '}{tournament.description}\n"
                          f"\n{'=' * 119}\n"
                          f"{'Tours'.center(119)}\n"
                          f"{'-' * 119}")

                    rounds = ["round_1", "round_2", "round_3", "round_4"]
                    for all_round in tournament.tours:

                        for key_round, value_round in all_round.items():

                            if key in rounds:
                                print(f"\n\n{key}\n{'-' * 11}")
                                i = 0
                                for current_round in value_round:

                                    print(f":: Match {i + 1} > Player N°{current_round[0][0]}:{current_round[0][2]} Vs "
                                          f"N°{current_round[1][0]}:{current_round[1][2]}")
                                    i += 1

    def choice_tournament(self, list_tournament: list) -> int:
        """
        Selects the tournament number to show
        """

        select_tournament = int(input(f"\n{'-' * 41}\n{':: Select the tournament to be modified > '}"))

        for key, value in enumerate(list_tournament):

            if key == select_tournament:
                self.menu.sub_menu(f"[ Tournament : {value.name} ] ")

                return key

    def result_round(self, list_tournament: list):
        """
        Changes the points of the completed rounds
        """

        select_tournament = int(input(f"\n{'-' * 41}\n{':: Select the tournament to be modified > '}"))

        for key, tournament in enumerate(list_tournament):

            if key == select_tournament:

                self.menu.sub_menu(f"[ Tournament : {tournament.name} ] ")

                results_round = list()

                str_round = f"round_{len(tournament.tours)}"
                round_indicator = len(tournament.tours) - 1

                print(f"{'Enter the points of the players of '}{str_round}\n{'-' * 42}")

                for number_match, match in enumerate(tournament.tours[round_indicator][str_round]):

                    print(f"\n[ Match {number_match + 1} ] Player N°{match[0][0]} Vs "
                          f"N°{match[1][0]}\n{'-' * 29}")

                    new_point_match_player_1 = float(utils.format_string(f"New point player N°{match[0][0]}"))
                    new_point_match_player_2 = float(utils.format_string(f"New point player N°{match[1][0]}"))

                    match[0], match[1] = list(match[0]), list(match[1])

                    match[0][2], match[1][2] = new_point_match_player_1, new_point_match_player_2

                    match[0], match[1] = tuple(match[0]), tuple(match[1])

                    results_round.append(match)

                tournament.tours[round_indicator][str_round] = results_round

                return key, results_round


if __name__ == "__main__":
    pass
