#! /usr/bin/env python3
# coding:utf-8

"""
import views
"""

import datetime

import models
import utils
import views


class ViewTournament:
    """
    Show and retrieve tournament information
    """

    TIMES_CONTROL = ["Blitz", "Bullet", "Quick hit"]

    def __init__(self):

        self.menu = views.ViewMenu()
        self.view_player = views.ViewPlayer()

    def main_tournament_info(self) -> tuple:
        """
        Add a tournament
        Retrieve name, location, date, description and time control of tournament
        """

        self.menu.sub_menu("* Add A Tournament *")

        name = utils.format_string("Name tournament").capitalize()
        location = utils.format_string("Location").capitalize()
        description = utils.format_string("Description").capitalize()

        date_string = (
            f"\nEnter start date\n{'-' * 16}",
            f"\nEnter end date\n{'-' * 14}",
        )

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

        return (
            name,
            location,
            start_date,
            end_date,
            time_control,
            description,
            nb_rounds,
        )

    def add_player_tournament(self, table_players) -> list:
        """
        Add player a tournament
        """

        self.view_player.view_show_player(table_players)

        print(
            f"\n{'Select players by their index to add them to the tournament'}\n"
            f"{'-' * 59}"
        )

        players = []

        for i in range(8):

            player = int(utils.format_string(f"Player {i + 1}"))
            players.append(player)

        return players

    def menu_tournament(self, list_tournament: list) -> None:
        """
        Show menu tournament
        """

        self.menu.sub_menu("Choice a tournament")

        for key, value in enumerate(list_tournament):
            print(f"[ {key} ] - [ {value.name}, {value.location} ]")

    def show_all_players_alphabetical(self, list_all_players: list[models.Player]) -> None:
        """
        Show all players alphabetical order
        """
        self.menu.show_menu()

        print(
            f"\n\n\n\n{'*** Players sorted alphabetically ***':^119}\n"
            f"{'°' * 119}\n"
            f"{'ID player':^15} | "
            f"{'Last name':^20} | "
            f"{'Name':^20} | "
            f"{'Birthday':^15} | "
            f"{'Sex':^10} | "
            f"{'Ranking':^10} | "
            f"{'Points':^10}"
            f"\n{'°' * 119}"
        )

        players = []
        for player in list_all_players:
            players.append(player)

        players_sorted_alphabetically = sorted(
            players, key=lambda x: x.last_name
        )

        for player in players_sorted_alphabetically:
            print(
                f"{player.player_id:^15} | "
                f"{player.last_name:^20} | "
                f"{player.name:^20} | "
                f"{player.birthday:^15} | "
                f"{player.sex:^10} | "
                f"{player.ranking:^10} | "
                f"{player.points:^10}"
            )

    def show_all_players_ranking(self, list_all_players: list[models.Player]) -> None:
        """
        Show all players by ranking order
        """

        self.menu.show_menu()

        print(
            f"\n\n\n\n{'*** Players sorted by ranking order ***':^119}\n"
            f"{'=' * 119}\n"
            f"{'ID player':^15} | "
            f"{'Last name':^20} | "
            f"{'Name':^20} | "
            f"{'Birthday':^15} | "
            f"{'Sex':^10} | "
            f"{'Ranking':^10} | "
            f"{'Points':^10}"
            f"\n{'°' * 119}"
        )

        players = []
        for player in list_all_players:
            players.append(player)

        players_sorted_ranking = sorted(players, key=lambda x: x.ranking)

        for player in players_sorted_ranking:
            print(
                f"{player.player_id:^15} | "
                f"{player.last_name:^20} | "
                f"{player.name:^20} | "
                f"{player.birthday:^15} | "
                f"{player.sex:^10} | "
                f"{player.ranking:^10} | "
                f"{player.points:^10}"
            )

    def show_all_players_alphabetical_by_tournament(self, list_all_tournaments: list[models.Tournament]) -> None:
        """
        Show all players alphabetical by tournament
        """

        self.menu.show_menu()
        self.menu_tournament(list_all_tournaments)

        select_tournament = self.choice_tournament(list_all_tournaments)

        for key, tournament in enumerate(list_all_tournaments):
            if key == select_tournament:

                print(
                    f"\n\n\n\n{'*** Players sorted by alphabetical order ***':^119}\n"
                    f"{'=' * 119}\n"
                    f"{'ID player':^15} | "
                    f"{'Last name':^20} | "
                    f"{'Name':^20} | "
                    f"{'Birthday':^15} | "
                    f"{'Sex':^10} | "
                    f"{'Ranking':^10} | "
                    f"{'Points':^10}"
                    f"\n{'°' * 119}"
                )

            players = []

            for player in tournament.players:
                players.append(player)

            players_sorted_ranking = sorted(players, key=lambda x: x.last_name)

            for player in players_sorted_ranking:
                print(
                    f"{player.player_id:^15} | "
                    f"{player.last_name:^20} | "
                    f"{player.name:^20} | "
                    f"{player.birthday:^15} | "
                    f"{player.sex:^10} | "
                    f"{player.ranking:^10} | "
                    f"{player.points:^10}"
                )

    def show_all_players_ranking_by_tournament(self, list_all_tournaments: list[models.Tournament]) -> None:
        """
        Show all players alphabetical by tournament
        """

        self.menu.show_menu()
        self.menu_tournament(list_all_tournaments)

        select_tournament = self.choice_tournament(list_all_tournaments)

        for key, tournament in enumerate(list_all_tournaments):
            if key == select_tournament:
                print(
                    f"\n\n\n\n{'*** Players sorted by alphabetical order ***':^119}\n"
                    f"{'=' * 119}\n"
                    f"{'ID player':^15} | "
                    f"{'Last name':^20} | "
                    f"{'Name':^20} | "
                    f"{'Birthday':^15} | "
                    f"{'Sex':^10} | "
                    f"{'Ranking':^10} | "
                    f"{'Points':^10}"
                    f"\n{'°' * 119}"
                )

            players = []

            for player in tournament.players:
                players.append(player)

            players_sorted_ranking = sorted(players, key=lambda x: x.ranking)

            for player in players_sorted_ranking:
                print(
                    f"{player.player_id:^15} | "
                    f"{player.last_name:^20} | "
                    f"{player.name:^20} | "
                    f"{player.birthday:^15} | "
                    f"{player.sex:^10} | "
                    f"{player.ranking:^10} | "
                    f"{player.points:^10}"
                )

    def show_all_tournaments(self, list_all_tournaments: list[models.Tournament]):
        """
        Show all tournaments
        """

        self.menu.show_menu()
        self.menu.sub_menu("List all tournaments")

        for key, tournament in enumerate(list_all_tournaments):

            print(f"[ {key} ] {tournament.name}  /  {tournament.location}  /  {tournament.description}  /  "
                  f"(Start : {tournament.start_date} / End : {tournament.end_date})\n{'-' * 119}")

    def show_all_match_by_tournaments(self, list_all_tournaments: list[models.Tournament]):
        """
        Show all match by tournaments
        """

        self.menu.show_menu()
        self.menu_tournament(list_all_tournaments)

        select_tournament = self.choice_tournament(list_all_tournaments)

        for key, tournament in enumerate(list_all_tournaments):
            if key == select_tournament:

                print(f"\n\n{'List of all matches'.center(119)}\n" f"{'=' * 119}")

                rounds = ["round_1", "round_2", "round_3", "round_4"]
                for all_round in tournament.tours:

                    for key_round, value_round in all_round.items():

                        if key_round in rounds:
                            print(
                                f"\n{key_round.title()}\n" f"{'-' * len(key_round)}"
                            )

                            i = 1
                            for player in value_round:
                                print(
                                    f"Match {i} : Player N°{player[0][0]} Vs player N°{player[1][0]}"
                                )
                                i += 1

    def show_all_rounds_by_tournaments(self, list_all_tournaments: list[models.Tournament]):
        """
        Show all rounds by tournaments
        """

        self.menu.show_menu()
        self.menu_tournament(list_all_tournaments)

        select_tournament = self.choice_tournament(list_all_tournaments)

        for key, tournament in enumerate(list_all_tournaments):
            if key == select_tournament:

                for all_rounds in tournament.tours:

                    for k, v in all_rounds.items():
                        print(f"\n[ {k} ]\n{v}")
                    print(f"\n{'-' * 119}")

    def choice_tournament(self, list_tournament: list) -> int:
        """
        Selects the tournament number to show
        """

        select_tournament = int(
            input(f"\n{'-' * 41}\n{':: Select the tournament to be modified > '}")
        )

        for key, value in enumerate(list_tournament):

            if key == select_tournament:
                self.menu.sub_menu(f"[ Tournament : {value.name} ] ")

                return key

    def result_round(self, list_tournament: list) -> tuple:
        """
        Changes the points of the completed rounds
        """

        select_tournament = self.choice_tournament(list_tournament)

        for id_tournament, tournament in enumerate(list_tournament):

            if id_tournament == select_tournament:

                self.menu.sub_menu(f"[ Tournament : {tournament.name} ] ")

                if tournament.state is False:
                    print("Tournament finnish")

                else:

                    results_round = list()
                    str_round = f"round_{len(tournament.tours)}"
                    round_indicator = len(tournament.tours) - 1

                    print(
                        f"{'Enter the points of the players of '}{str_round}\n{'-' * 42}"
                    )

                    for number_match, match in enumerate(
                        tournament.tours[round_indicator][str_round]
                    ):

                        print(
                            f"\n[ Match {number_match + 1} ] Player N°{match[0][0]} Vs "
                            f"N°{match[1][0]}\n{'-' * 29}"
                        )

                        new_point_match_player_1 = float(
                            utils.format_string(f"New point player N°{match[0][0]}")
                        )
                        new_point_match_player_2 = float(
                            utils.format_string(f"New point player N°{match[1][0]}")
                        )

                        match[0], match[1] = list(match[0]), list(match[1])

                        match[0][2], match[1][2] = (
                            new_point_match_player_1,
                            new_point_match_player_2,
                        )

                        match[0], match[1] = tuple(match[0]), tuple(match[1])

                        results_round.append(match)

                    return id_tournament, round_indicator, str_round, results_round


if __name__ == "__main__":
    pass
