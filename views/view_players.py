#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
"""

from tinydb import Query
import datetime

import views.view_menu
import models.models


class ViewPlayer:

    @staticmethod
    def show():

        views.view_menu.ShowMenu.menu()

        print(f"\n\n{'=' * 119}\n"
              f"{'|'}{'* List of all players *'.center(117)}{'|'}\n"
              f"{'-' * 119}\n\n"
              f"{'ID'.center(10)} | "
              f"{'Last name'.center(25)} | "
              f"{'Name'.center(25)} | "
              f"{'Birthday'.center(20)} | "
              f"{'Sex'.center(10)} | "
              f"{'Ranking'.center(10)}"
              f"\n{'~' * 119}")

        for player in models.models.PLAYERS:
            print(f"{str(player.doc_id).center(10)} | "
                  f"{player['Last_name'].center(25)} | "
                  f"{player['Name'].center(25)} | "
                  f"{player['Birthday'].center(20)} | "
                  f"{player['Sex'].center(10)} | "
                  f"{str(player['Ranking']).center(10)}")

        print(f"\n{'-' * 119}")

    @staticmethod
    def add():

        views.view_menu.ShowMenu.menu()

        player = {}

        while 1:

            print(f"\n\n{'=' * 119}\n"
                  f"{'|'}{'* Add A Player *'.center(117)}{'|'}\n"
                  f"{'-' * 119}")

            try:
                last_name = input('- Last name : ').capitalize()
                name = input('- Name : ').capitalize()
                print(f"\n{'Birth date'}\n"
                      f"{'-' * 10}")
                year = int(input("- Year : "))
                month = int(input("- Month : "))
                day = int(input("- Day : "))
                birth_day = datetime.date(year, month, day)
                sex = input('\n- Sex [F/M] : ').capitalize()

                if sex not in "FM":
                    print(f"""\n{":: ERROR > Enter a valid form. Ex: 'F' for female and 'M' for male for Sex"}\n""")
                    continue

            except ValueError:
                print(f"\n{':: ERROR > Enter a valid date of birth like this'}\n"
                      f"{'-' * 48}\n"
                      f"{'Year : 1979'}\n"
                      f"{'Month : 07'}\n"
                      f"{'Day : 13'}\n")
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
    def remove():

        views.view_players.ViewPlayer.show()

        player_q = Query()

        choice_player = input('Select the player ID to be deleted : ')
        choice_player = int(choice_player)

        id_player = models.models.PLAYERS.get(doc_id=choice_player)

        models.models.PLAYERS.remove(player_q.Last_name == id_player["Last_name"])

        views.view_menu.ShowMenu.menu()

    @staticmethod
    def ranking():

        views.view_players.ViewPlayer.show()

        ranking_q = Query()

        id_player = input('Select player ID to change rank : ')
        id_player = int(id_player)

        player = models.models.PLAYERS.get(doc_id=id_player)

        new_ranking = input('New ranking : ')
        new_ranking = int(new_ranking)

        models.models.PLAYERS.update({'Ranking': new_ranking}, ranking_q.Ranking == player['Ranking'])

        views.view_players.ViewPlayer.show()


if __name__ == "__main__":
    pass
