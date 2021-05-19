#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
"""
import json
from tinydb import Query
import datetime

import views.view_menu
import models.models_players


class ViewPlayer:

    all_players = models.models_players.DeserializePlayer.players(models.models_players.PLAYERS.all())

    @staticmethod
    def show():

        views.view_menu.ShowMenu.menu()

        views.view_menu.ShowMenu.sub_menu('* List of all players *')

        print(f"{'ID'.center(10)} | "
              f"{'Last name'.center(25)} | "
              f"{'Name'.center(25)} | "
              f"{'Birthday'.center(20)} | "
              f"{'Sex'.center(10)} | "
              f"{'Ranking'.center(10)}"
              f"\n{'°' * 119}")

        for key, player in enumerate(ViewPlayer.all_players):
            print(f"{str(key).center(10)} | "
                  f"{player['Last_name'].center(25)} | "
                  f"{player['Name'].center(25)} | "
                  f"{player['Birthday'].center(20)} | "
                  f"{player['Sex'].center(10)} | "
                  f"{str(player['Ranking']).center(10)}"
                  f"\n{'-' * 119}")

    @staticmethod
    def add():

        views.view_menu.ShowMenu.menu()

        player = {}

        while 1:

            views.view_menu.ShowMenu.sub_menu('* Add A Player *')

            try:
                last_name = views.view_menu.ShowMenu.get_string_value('Last name').capitalize()
                name = views.view_menu.ShowMenu.get_string_value('Name').capitalize()
                print(f"\n{'Birth date'}\n"
                      f"{'-' * 10}")
                year = int(views.view_menu.ShowMenu.get_string_value('Year'))
                month = int(views.view_menu.ShowMenu.get_string_value('Month'))
                day = int(views.view_menu.ShowMenu.get_string_value('Day'))
                birth_day = datetime.date(year, month, day)
                print()
                sex = views.view_menu.ShowMenu.get_string_value('Sex [F/M]').capitalize()

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
                ranking = int(views.view_menu.ShowMenu.get_string_value(ranking))

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

        id_player = models.models_players.PLAYERS.get(doc_id=choice_player)

        print(f"\nRemove the next player\n"
              f"{'-' * 22}")

        for player in id_player.values():
            print(f"- {player}")

        accept_delete = input('\nDelete player [o/N] : ')

        if accept_delete and accept_delete in "Oo":
            models.models_players.PLAYERS.remove(player_q.Last_name == id_player["Last_name"])

        views.view_menu.ShowMenu.menu()

    @staticmethod
    def new_ranking():

        views.view_players.ViewPlayer.show()

        id_player = input('Select player ID to change rank : ')
        id_player = int(id_player)

        for player_id, player in enumerate(ViewPlayer.all_players):
            if id_player == player_id:
                new_ranking = input('New ranking : ')
                new_ranking = int(new_ranking)
                player['Ranking'] = new_ranking

        views.view_menu.ShowMenu.menu()


if __name__ == "__main__":
    pass
