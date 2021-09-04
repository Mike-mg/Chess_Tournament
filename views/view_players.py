#! /usr/bin/env python3
# coding:utf-8

import views
import utils
import controllers


class ViewPlayer:
    """
    Show and retrieves player information
    """

    def __init__(self):

        self.view_menu = views.ViewMenu()

    def view_show_player(self):
        """
        Show all players
        """

        self.view_menu.show_menu()
        self.view_menu.sub_menu('* List of all players *')

        print(f"{'ID'.center(10)} | "
              f"{'Last name'.center(20)} | "
              f"{'Name'.center(20)} | "
              f"{'Birthday'.center(15)} | "
              f"{'Sex'.center(10)} | "
              f"{'Ranking'.center(10)} | "
              f"{'Points'.center(10)}"
              f"\n{'°' * 119}")

        for key, player in enumerate(controllers.ControllerPlayer.ALL_PLAYERS):

            print(f"{str(key).center(10)} | "
                  f"{player.last_name.center(20)} | "
                  f"{player.name.center(20)} | "
                  f"{player.birthday.center(15)} | "
                  f"{player.sex.center(10)} | "
                  f"{str(player.ranking).center(10)} | "
                  f"{str(player.points).center(10)}"
                  f"\n{'-' * 119}")

    def add_player(self) -> tuple:
        """
        Add a player
        """

        self.view_menu.show_menu()
        self.view_menu.sub_menu("* Add A Player *")

        last_name = utils.utils_func.format_string("Last name")
        name = utils.utils_func.format_string("Name")
        birthday = utils.utils_func.format_string("Birthday")
        sex = utils.utils_func.format_string("Sex")
        ranking = int(utils.utils_func.format_string("Ranking"))
        points = 0

        return last_name, name, birthday, sex, ranking, points

    def new_player_ranking(self, all_players: list):
        """
        Modified ranking player
        """

        self.view_show_player()

        select_player = int(input(f"\n{'-' * 41}\n{':: Select the player to be modified > '}"))

        for key, player in enumerate(all_players):

            if key == select_player:
                print(f"\n{'Select player :'} {player.last_name} {player.name}\n{'-' * 30}")

                new_ranking = int(input('Enter the new ranking : '))

                player.ranking = new_ranking


if __name__ == "__main__":
    pass
