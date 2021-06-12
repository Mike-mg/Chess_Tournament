#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
"""

import datetime

import views.view_menu
import models.models_players


def format_string(get_string):
    return input(f":: {get_string} > ")


def view_show_player(table_players=models.models_players.table_players.all()):
    """
    View show all player
    """

    all_players = table_players

    views.view_menu.show_menu()

    views.view_menu.sub_menu('* List of all players *')

    print(f"{'ID'.center(10)} | "
          f"{'Last name'.center(20)} | "
          f"{'Name'.center(20)} | "
          f"{'Birthday'.center(15)} | "
          f"{'Sex'.center(10)} | "
          f"{'Ranking'.center(10)} | "
          f"{'Points'.center(10)}"
          f"\n{'°' * 119}")

    for key, player in enumerate(all_players):

        print(f"{str(key).center(10)} | "
              f"{player['Last_name'].center(20)} | "
              f"{player['Name'].center(20)} | "
              f"{player['Birthday'].center(15)} | "
              f"{player['Sex'].center(10)} | "
              f"{str(player['Ranking']).center(10)} | "
              f"{str(player['Points']).center(10)}"
              f"\n{'-' * 119}")


def add_player():
    """
    Docstings
    """
    views.view_menu.show_menu()

    views.view_menu.sub_menu("* Add A Player *")

    last_name = format_string("Last name")
    name = format_string("Name")
    birthday = format_string("Birthday")
    sex = format_string("Sex")
    ranking = format_string("Ranking")
    points = 0

    return (last_name, name, birthday, sex, ranking, points)

# def view_add_player_tournament():
#     """
#     View add player
#     """
#
#     views.view_menu.show_menu()
#     views.view_menu.sub_menu('* Add A Player *')
#
#     player_list = list()
#
#     nb_player = int(format_string("Number of players in the tournament : "))
#
#     for player in range(nb_player):
#
#         player_dict = dict()
#
#         player_dict["Last_name"] = format_string('\n- Last name : ').capitalize()
#         player_dict["Name"] = str(format_string('- Name : ')).capitalize()
#         print(f"\n{'Birth date'}\n"
#               f"{'-' * 10}")
#         year = int(format_string('- Year : '))
#         month = int(format_string('- Month : '))
#         day = int(format_string('- Day : '))
#         player_dict["birthday"] = datetime.date(year, month, day).strftime("%d/%m/%Y")
#         player_dict["Sex"] = format_string('\n- Sex [F/M] : ').capitalize()
#         player_dict["Ranking"] = int(format_string('- Ranking : '))
#         player_dict["Points"] = int(format_string('- Points : '))
#
#         player_list.append(player_dict)
#
#     return player_list


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
