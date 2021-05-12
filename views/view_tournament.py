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

            name = input(f"Name tournament : ")
            location = input(f"Location : ")
            print(f"\n{'Enter start date'}\n"
                  f"{'-' * 16}")

            try:

                start_date = datetime.date(int(input("- Year : ")), int(input("- Month : ")), int(input("- Day : ")))

                print(f"\n{'Enter end date'}\n"
                      f"{'-' * 14}")
                end_date = datetime.date(int(input("- Year : ")), int(input("- Month : ")), int(input("- Day : ")))

                start_date.strftime("%d/%m/%Y")
                end_date.strftime("%d/%m/%Y")

            except ValueError:
                print(f"\n{':: ERROR > Enter a valid date of birth like this'}\n"
                      f"{'-' * 48}\n"
                      f"{'Year : 1979'}\n"
                      f"{'Month : 07'}\n"
                      f"{'Day : 13'}\n")
                continue

            players = ViewTournament.add_player_tournament()

            nb_rounds = input(f"""\n{"NB rounds ( default '4' ) : "}""")

            try:

                if not nb_rounds:
                    nb_rounds = 4

            except ValueError:
                print(f"\n{':: ERROR > Enter a valid format, the rank must be a positive number'}\n")
                continue

            tournament["Name"] = name
            tournament["Location"] = location
            tournament["Start date"] = str(start_date.strftime("%d/%m/%Y"))
            tournament["End date"] = str(end_date.strftime("%d/%m/%Y"))
            tournament["Players"] = players
            tournament["Nb_rounds"] = nb_rounds

            break

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
                  f"{player['Ranking']}")


        print()

        for i in range(8):

            try:
                player = int(input(f"{'Player N°'}{i + 1} :  "))

            except ValueError:
                print(f"\n{':: ERROR > Enter a valid format, the rank must be a positive number'}\n")
                continue

            players.append(player)

        return players
