#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
"""
import datetime

import models.models_players
import views.view_menu


def format_string(get_string):
    return input(f"- {get_string} : ")


class ViewShowPlayer:
    """
    View show all player
    """

    def __init__(self, table_players):

        self.table_players = table_players

    def show_players(self):

        views.view_menu.ShowMenu()

        views.view_menu.SubMenu('* List of all players *')

        print(f"{'ID'.center(10)} | "
              f"{'Last name'.center(25)} | "
              f"{'Name'.center(25)} | "
              f"{'Birthday'.center(20)} | "
              f"{'Sex'.center(10)} | "
              f"{'Ranking'.center(10)}"
              f"\n{'°' * 119}")

        for player in self.table_players:
            print(f"{str(player.doc_id).center(10)} | "
                  f"{player['Last_name'].center(25)} | "
                  f"{player['Name'].center(25)} | "
                  f"{player['Birthday'].center(20)} | "
                  f"{player['Sex'].center(10)} | "
                  f"{str(player['Ranking']).center(10)}"
                  f"\n{'-' * 119}")


class ViewAddPlayer:
    """
    View add player
    """

    def __init__(self):

        views.view_menu.ShowMenu()

        player = {}

        while 1:

            views.view_menu.SubMenu('* Add A Player *')

            try:
                self.last_name = format_string('Last name').capitalize()
                self.name = str(format_string('Name')).capitalize()
                print(f"\n{'Birth date'}\n"
                      f"{'-' * 10}")
                year = int(format_string('Year'))
                month = int(format_string('Month'))
                day = int(format_string('Day'))
                self.birthday = datetime.date(year, month, day).strftime("%d/%m/%Y")
                print()
                self.sex = format_string('Sex [F/M]').capitalize()

                if self.sex not in "FM":
                    print(f"""\n{":: ERROR > Enter a valid form. Ex: 'F' for female and 'M' for male for Sex"}\n""")
                    continue

            except ValueError:
                print(f"\n{':: ERROR > Enter a valid date of birth like this'}\n"
                      f"{'-' * 48}\n"
                      f"{'Year : 1979'}\n"
                      f"{'Month : 07'}\n"
                      f"{'Day : 13'}\n")
                continue

            self.ranking = f"{input('- Ranking : ')}"

            try:
                self.ranking = int(self.ranking)

            except ValueError:
                print(f"\n{':: ERROR > Enter a valid format, the rank must be a positive number'}\n")
                continue

            player["Last_name"] = self.last_name
            player["Name"] = self.name
            player["Birthday"] = self.birthday
            player["Sex"] = self.sex
            player["Ranking"] = self.ranking

            break


class ViewRemovePlayer:
    """
    View remove player
    """

    def __init__(self):

        self.id_player_remove = int()

    def remove_player(self):

        views.view_players.ViewShowPlayer(models.models_players.table_players.all())

        choice_player = input('Select the player ID to be deleted : ')
        choice_player = int(choice_player)

        id_player = models.models_players.table_players.get(doc_id=choice_player)
        self.id_player_remove = id_player.doc_id

        views.view_menu.ShowMenu()


class ViewRankingPlayer:
    """
    View new ranking player
    """
    def __init__(self):

        self.player_id = int()
        self.ranking = int()

    def new_ranking(self):

        views.view_players.ViewShowPlayer(models.models_players.table_players.all())

        id_player = input('Select player ID to change rank : ')
        id_player = int(id_player)

        new_ranking = input('New ranking : ')
        new_ranking = int(new_ranking)

        self.player_id = id_player
        self.ranking = new_ranking

        views.view_menu.ShowMenu()


if __name__ == "__main__":
    pass
