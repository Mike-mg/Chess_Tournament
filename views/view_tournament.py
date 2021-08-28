#! /usr/bin/env python3
# coding:utf-8

"""
import views
"""

import datetime

import controllers.controller_tournament
import views.view_players
import views.view_menu



def format_string(get_string):
    return input(f":: {get_string} > ")


class ViewTournament:
    """
    Objet view tournament
    """

    def __init__(self):

        self.menu = views.view_menu.ViewMenu()
        self.view_player = views.view_players.ViewPlayer()

    def menu_tournament(self, list_tournament):
        """
        Show menu tournament
        """

        # views.view_menu.show_menu()
        self.menu.sub_menu("Current tournament")

        for key, value in enumerate(list_tournament):
            print(f"[ {key} ] - [ {value.name}, {value.location} ]")

    def main_tournament_info(self):
        """
        Name, location, date, description and time control of tournament
        """

        # views.view_menu.show_menu()
        self.menu.sub_menu('* Add A Tournament *')

        name = format_string("Name tournament").capitalize()
        location = format_string("Location").capitalize()
        description = format_string("Description").capitalize()

        date_string = (f"\nEnter start date\n{'-' * 16}",
                       f"\nEnter end date\n{'-' * 14}")

        date = []

        for value in date_string:

            print(value)

            year = int(format_string("Year"))
            month = int(format_string("Month"))
            day = int(format_string("Day"))
            date.append(datetime.date(year, month, day).strftime("%d/%m/%Y"))

        start_date = date[0]
        end_date = date[1]

        list_time_control = ["Blitz", "Bullet", "Quick hit"]

        print(f"\nSelect time control\n{'-' * 19}")

        for key, time_control in enumerate(list_time_control):
            print(f"[ {key} ]  {time_control}")

        choice_time_control = int(format_string("Choice time control"))

        time_control = list_time_control[choice_time_control]

        return name, location, start_date, end_date, time_control, description

    def add_player_tournament(self):
        """
        Add player at a tournament
        """

        self.view_player.view_show_player()

        print(f"\n{'Select players by their index to add them to the tournament'}\n"
              f"{'-' * 59}")

        players = []

        for i in range(8):

            player = int(format_string(f"Player {i + 1}"))

            players.append(player)

        return players

    def show_tournament(self, list_tournament):

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

                for all_round in tournament.tours:
                    for value_id, value in all_round.items():
                        print(f"\n\n[ {value_id} ]\n{'-' * 11}")

                        i = 0
                        for current_round in value:
                            print(f":: Match {i + 1} > Player N°{current_round[0][0]}:{current_round[0][2]} Vs "
                                  f"N°{current_round[1][0]}:{current_round[1][2]}")
                            i += 1

    def result_round(self, list_tournament):

        results_round = []
        key_tournament = int()

        select_tournament = int(input(f"\n{'-' * 41}\n{':: Select the tournament to be modified > '}"))

        for key, value in enumerate(list_tournament):

            if key == select_tournament:
                key_tournament = key

                str_round = str()

                if  value.round_indicator == 0:
                    str_round = "Round_1"

                elif value.round_indicator == 1:
                    str_round = "Round_2"
                #
                # elif value.round_indicator == 2:
                #     str_round = "Round_3"
                #
                # elif value.round_indicator == 3:
                #     str_round = "Round_4"

                self.menu.sub_menu(f"[ Tournament : {value.name} ]  {str_round} {'results'}")

                print(f"{'Enter the points of the players in '}{str_round}\n{'-' * 42}")

                for number_match, match in enumerate(value.tours[value.round_indicator][str_round]):

                    print(f"\n[ Match {number_match + 1} ] Player N°{match[0][0]} Vs "
                          f"N°{match[1][0]}\n{'-' * 29}")

                    new_point_match_player_1 = float(format_string(f"New point player N°{match[0][0]}"))
                    new_point_match_player_2 = float(format_string(f"New point player N°{match[1][0]}"))

                    match[0], match[1] = list(match[0]), list(match[1])

                    match[0][2], match[1][2] = new_point_match_player_1, new_point_match_player_2

                    match[0], match[1] = tuple(match[0]), tuple(match[1])

                    results_round.append(match)

            value.round_indicator += 1

        return key_tournament, results_round


if __name__ == "__main__":
    pass
