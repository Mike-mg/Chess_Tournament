#! /usr/bin/env python3
# coding:utf-8

"""
import views
"""

import datetime

import views.view_menu
import models.models


class ViewTournament:

    @staticmethod
    def add_tournament():

        views.view_menu.ShowMenu.menu()

        tournament = {}

        while 1:

            print(f"\n\n{'=' * 119}\n"
                  f"{'|'}{'* Add A Tournament *'.center(117)}{'|'}\n"
                  f"{'-' * 119}")

            name = ViewTournament.name_tournament()
            location = ViewTournament.location_tournament()
            date_start_end = ViewTournament.date_tournament()
            players = ViewTournament.add_player_tournament()
            nb_rounds = ViewTournament.nb_rounds()
            tours = ViewTournament.tours(players)

            tournament["Name"] = name
            tournament["Location"] = location
            tournament["Start date"] = date_start_end[0]
            tournament["End date"] = date_start_end[1]
            tournament["Players"] = players
            tournament["Nb_rounds"] = nb_rounds
            tournament["Tours"] = tours

            return tournament

    @staticmethod
    def add_player_tournament():

        players = []

        print(f"\n{'Select players by their index to add them to the tournament'}\n"
              f"{'-' * 59}")

        for player in models.models.DB_ALL_PLAYERS:
            print(f"[ {player.doc_id} ] "
                  f"{player['Last name']}, "
                  f"{player['Name']}, "
                  f"{player['Birthday']}, "
                  f"{player['Sex']}, "
                  f"{player['Ranking']}\n")

        for i in range(8):

            try:
                player = int(input(f"{'Player N°'}{i + 1} :  "))

            except ValueError:
                print(f"\n{':: ERROR > Enter a valid format, the rank must be a positive number'}\n")
                continue

            players.append(player)

        return players

    @staticmethod
    def name_tournament():

        name = input(f"- Name tournament : ")
        return name

    @staticmethod
    def location_tournament():

        location = input(f"- Location : ")
        return location

    @staticmethod
    def date_tournament():

        date = []

        try:
            print(f"\n{'Enter start date'}\n"
                  f"{'-' * 16}")

            start_date = datetime.date(int(input("- Year : ")), int(input("- Month : ")), int(input("- Day : ")))

            print(f"\n{'Enter end date'}\n"
                  f"{'-' * 14}")
            end_date = datetime.date(int(input("- Year : ")), int(input("- Month : ")), int(input("- Day : ")))

            start_date = start_date.strftime("%d/%m/%Y")
            end_date = end_date.strftime("%d/%m/%Y")

            date.append(start_date)
            date.append(end_date)

        except ValueError:
            print(f"\n{':: ERROR > Enter a valid date of birth like this'}\n"
                  f"{'-' * 48}\n"
                  f"{'Year : 1979'}\n"
                  f"{'Month : 07'}\n"
                  f"{'Day : 13'}\n")
        return date

    @staticmethod
    def nb_rounds():

        nb_rounds = input(f"""\n{"NB rounds ( default '4' ) : "}""")

        try:

            if not nb_rounds:
                nb_rounds = 4

        except ValueError:
            print(f"\n{':: ERROR > Enter a valid format, the rank must be a positive number'}\n")

        return nb_rounds

    @staticmethod
    def tours(players):

        round1 = {1: [
            [{"Player": players[0], "Points": 0}, {"Player": players[4], "Points": 0}],
            [{"Player": players[1], "Points": 0}, {"Player": players[5], "Points": 0}],
            [{"Player": players[2], "Points": 0}, {"Player": players[6], "Points": 0}],
            [{"Player": players[3], "Points": 0}, {"Player": players[7], "Points": 0}]
        ]}

        return round1

    @staticmethod
    def show_all_tournament():

        print(f"\n{'=' * 119}\n"
              f"{'|'}{'* List of all tournaments *'.center(117)}{'|'}\n"
              f"{'-' * 119}\n\n")

        for tournament in models.models.DB_ALL_TOURNAMENTS:
            print(f"{'=' * 35}\n"
                  f"N° : {str(tournament.doc_id)}\n"
                  f"Name : {tournament['Name']}\n"
                  f"Location : {tournament['Location']}\n"
                  f"Start date : {tournament['Start date']}\n"
                  f"End date : {tournament['End date']}\n"
                  f"Players : {tournament['Players']}\n"
                  f"Nb rounds : {tournament['Nb_rounds']}\n")

            for rounds in tournament['Tours']:

                print(f"Round : {rounds}")

                for round_key, round_value in tournament['Tours'][rounds]:
                    print(f"Player {round_key['Player']} (Pts = {round_key['Points']}) Vs "
                          f"{round_value['Player']} (Pts = {round_value['Points']})")

            print(f"{'-' * 35}\n\n")

    @staticmethod
    def point_round_1():

        views.view_menu.ShowMenu.menu()

        print(f"\n\n{'=' * 119}\n"
              f"{'|'}{'* Modified Current Tournament *'.center(117)}{'|'}\n"
              f"{'-' * 119}")

        tournament_list = [
            'Show all tournaments',
            'Show per tournament',
        ]

        for index, m_menu in enumerate(tournament_list):
            print(f"{':: '}{index} > {m_menu}")

        choice_tournament = input("\nTournament modified : ")

        try:
            choice_tournament = int(choice_tournament)

        except ValueError:
            print(f"\n{':: ERROR > Enter a valid format, the rank must be a positive number'}\n")

        if choice_tournament == 0:
            ViewTournament.show_all_tournament()


        elif choice_tournament == 1:
            for tournament in models.models.DB_ALL_TOURNAMENTS:
                print(tournament)


if __name__ == "__main__":
    pass
