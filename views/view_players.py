#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
"""

import datetime

import views.view_menu
import models.models_players


def format_string(get_string):
    return input(f"{get_string}")


def view_show_player(table_players):
    """
    View show all player
    """

    views.view_menu.show_menu()

    views.view_menu.sub_menu('* List of all players *')

    print(f"{'ID'.center(10)} | "
          f"{'Last name'.center(25)} | "
          f"{'Name'.center(25)} | "
          f"{'Birthday'.center(20)} | "
          f"{'Sex'.center(10)} | "
          f"{'Ranking'.center(10)}"
          f"\n{'°' * 119}")

    for player in table_players:
        print(f"{str(player.doc_id).center(10)} | "
              f"{player['Last_name'].center(25)} | "
              f"{player['Name'].center(25)} | "
              f"{player['Birthday'].center(20)} | "
              f"{player['Sex'].center(10)} | "
              f"{str(player['Ranking']).center(10)}"
              f"\n{'-' * 119}")


def view_add_player():
    """
    View add player
    """

    views.view_menu.show_menu()
    views.view_menu.sub_menu('* Add A Player *')

    player_list = list()
    nb_player = int(format_string("Number of players in the tournament : "))

    for player in range(nb_player):

        player_dict = dict()

        player_dict["Last_name"] = format_string('\n- Last name : ').capitalize()
        player_dict["Name"] = str(format_string('- Name : ')).capitalize()
        print(f"\n{'Birth date'}\n"
              f"{'-' * 10}")
        year = int(format_string('- Year : '))
        month = int(format_string('- Month : '))
        day = int(format_string('- Day : '))
        player_dict["birthday"] = datetime.date(year, month, day).strftime("%d/%m/%Y")
        player_dict["Sex"] = format_string('\n- Sex [F/M] : ').capitalize()
        player_dict["Ranking"] = int(format_string('- Ranking : '))

        player_list.append(player_dict)

    return player_list


class ViewRankingPlayer:
    """
    View new ranking player
    """
    def __init__(self):

        self.player_id = int()
        self.ranking = int()

    def new_ranking(self):

        views.view_players.view_show_player(models.models_players.table_players.all())

        id_player = input(':: Select player ID to change rank > ')
        id_player = int(id_player)

        new_ranking = input(':: New ranking > ')
        new_ranking = int(new_ranking)

        self.player_id = id_player
        self.ranking = new_ranking

        views.view_menu.show_menu()


if __name__ == "__main__":
    pass
