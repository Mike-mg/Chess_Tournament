#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
"""

import datetime

import views.view_menu
import models.models


class ViewPlayer:

    @staticmethod
    def add_player():

        views.view_menu.ShowMenu.menu()

        player = {}

        while 1:

            print(f"\n\n{'=' * 119}\n"
                  f"{'|'}{'* Add A Player *'.center(117)}{'|'}\n"
                  f"{'-' * 119}")

            last_name = f"{input('- Last name : ').capitalize()}"
            name = f"{input('- Name : ').capitalize()}"

            try:
                birth_day = datetime.date(int(input("- Year : ")), int(input("- Month : ")), int(input("- Day : ")))

            except ValueError:
                print(f"\n{':: ERROR > Enter a valid date of birth like this'}\n"
                      f"{'-' * 48}\n"
                      f"{'Year : 1979'}\n"
                      f"{'Month : 07'}\n"
                      f"{'Day : 13'}\n")
                continue

            sex = f"{input('- Sex [F/M] : ').capitalize()}"

            if sex not in "FM":
                print(f"""\n{":: ERROR > Enter a valid form. Ex: 'F' for female and 'M' for male for Sex"}\n""")
                continue

            ranking = f"{input('- Ranking : ')}"

            try:
                ranking = int(ranking)

            except ValueError:
                print(f"\n{':: ERROR > Enter a valid format, the rank must be a positive number'}\n")
                continue

            player["last_name"] = last_name
            player["name"] = name
            player["birth_day"] = str(birth_day.strftime("%d/%m/%Y"))
            player["sex"] = sex
            player["ranking"] = ranking

            break

        return player

    @staticmethod
    def show_players():

        views.view_menu.ShowMenu.menu()

        print(f"\n\n{'=' * 119}\n"
              f"{'|'}{'* List of all players *'.center(117)}{'|'}\n"
              f"{'-' * 119}\n\n"
              f"{'N°'.center(10)} | "
              f"{'Last name'.center(25)} | "
              f"{'Name'.center(25)} | "
              f"{'Birthday'.center(20)} | "
              f"{'Sex'.center(10)} | "
              f"{'Ranking'.center(10)}"
              f"\n{'~' * 119}")

        for player in models.models.DB_ALL_PLAYERS:
            print(f"{str(player.doc_id).center(10)} | "
                  f"{player['Last name'].center(25)} | "
                  f"{player['Name'].center(25)} | "
                  f"{player['Birthday'].center(20)} | "
                  f"{player['Sex'].center(10)} | "
                  f"{str(player['Ranking']).center(10)}")

        print(f"\n{'-' * 119}")


if __name__ == "__main__":
    pass
