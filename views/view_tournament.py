#! /usr/bin/env python3
# coding:utf-8

"""
import views
"""

import datetime

import views.view_players
import views.view_menu
import models.models_players
import models.models_tournaments


class ViewTournament:

    @staticmethod
    def add_tournament():

        views.view_menu.ShowMenu.menu()

        tournament = {}

        while 1:

            views.view_menu.ShowMenu.sub_menu('* Add A Tournament *')

            name = views.view_menu.ShowMenu.get_string_value("Name Tournament")
            location = views.view_menu.ShowMenu.get_string_value("Location")
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

        views.view_players.ViewPlayer.show()

        players = []

        print(f"\n{'Select players by their index to add them to the tournament'}\n"
              f"{'-' * 59}")

        for i in range(8):

            try:
                player = int(input(f"{'Player N°'}{i + 1} :  "))

            except ValueError:
                print(f"\n{':: ERROR > Enter a valid format, the rank must be a positive number'}\n")
                continue

            players.append(player)

        return players

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

        views.view_menu.ShowMenu.menu()
        views.view_menu.ShowMenu.sub_menu('* List of all tournaments *')

        for tournament in models.models_tournaments.TOURNAMENTS:
            print(f"\n{'=' * 35}\n"
                  f"ID : {str(tournament.doc_id)}\n"
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

            print(f"{'-' * 35}")

    @staticmethod
    def point_round_1():

        views.view_menu.ShowMenu.menu()
        views.view_menu.ShowMenu.sub_menu('* Modified Current Tournament *')
        ViewTournament.show_all_tournament()

        choice_tournament = input('ID tournament : ')
        choice_tournament = int(choice_tournament)

        tournament = models.models_tournaments.TOURNAMENTS.get(doc_id=choice_tournament)
        print(type(tournament))

if __name__ == "__main__":
    pass
