#! usr/bin/env python3
# coding:utf-8

import view
import data_base

"""Docstring"""


class BColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Player:

    """Docstring"""

    PLAYER = {}

    def __init__(self, last_name, name, birthday, sex, ranking):
        self.last_name = last_name.capitalize()
        self.name = name.capitalize()
        self.birthday = birthday
        self.sex = sex.capitalize()
        self.ranking = int(ranking)

        Player.PLAYER['Last name'] = self.last_name
        Player.PLAYER['Name'] = self.name
        Player.PLAYER['Birthday'] = self.birthday
        Player.PLAYER['Sex'] = self.sex
        Player.PLAYER['Ranking'] = self.ranking

        data_base.DB_ALL_PLAYERS.insert(Player.PLAYER)

    @classmethod
    def add_player(cls):

        while True:

            print(f"\n\n{'#' * 119}"
                  f"\n| Add a player |",
                  f"\n{'################'}\n")
            Player(input("Last name : "),
                   input("Name : "),
                   input(f"Date of birth {BColors.WARNING}(Ex '01/01/20'){BColors.END} : "),
                   input(f"Sex {BColors.WARNING}(Ex : 'M/F'){BColors.END} : "),
                   int(input("Ranking : ")))

            choice = input(f"\n{BColors.BOLD}{BColors.GREEN}"
                           f"{'# Add another player [O/n] : '}{BColors.END}")

            if choice in "Oo":
                continue
            else:
                view.ShowMenu.menu()
                return False

    @classmethod
    def show_players(cls):
        print(f"\n\n{'#' * 119}"
              f"\n| Show all players |"
              f"\n{'####################'}\n\n"
              f"{'N°'.center(10)} | " 
              f"{'Last name'.center(25)} | "
              f"{'Name'.center(25)} | "
              f"{'Birthday'.center(20)} | "
              f"{'Sex'.center(10)} | "
              f"{'Ranking'.center(10)}"
              f"\n{'*' * 119}")

        for player in data_base.DB_ALL_PLAYERS:
            print(f"{str(player.doc_id).center(10)} | "
                  f"{player['Last name'].center(25)} | "
                  f"{player['Name'].center(25)} | "
                  f"{player['Birthday'].center(20)} | "
                  f"{player['Sex'].center(10)} | "
                  f"{str(player['Ranking']).center(10)}")

        print(f"\n{'#' * 119}")

    # player_1 = Player("Dupont", "Nicolas", "13/07/72", "M", 0)
    # player_2 = Player("Miller", "Emma", "14/01/73", "F", 0)
    # player_3 = Player("Lopez", "Olivia", "15/02/74", "F", 0)
    # player_4 = Player("Roux", "Michael", "16/03/75", "M", 0)
    # player_5 = Player("Hall", "Pierre", "17/04/76", "M", 0)
    # player_6 = Player("Roy", "Jade", "18/05/77", "F", 0)
    # player_7 = Player("Rey", "Léo", "19/06/78", "M", 0)
    # player_8 = Player("Connor", "Manon", "20/07/79", "F", 0)


class Tournament:

    """Docstring"""

    TOURNAMENT = {}

    def __init__(self, name_tournament, location, date, players, nb_tours, time_control, description, nb_rounds=4):
        self.name = name_tournament.title()
        self.location = location.title()
        self.date = date
        self.players = players
        self.nb_rounds = nb_rounds
        self.nb_tours = nb_tours
        self.time_control = time_control
        self.description = description.title()

        Tournament.TOURNAMENT['Name'] = self.name
        Tournament.TOURNAMENT['Location'] = self.location
        Tournament.TOURNAMENT['Date'] = self.date
        Tournament.TOURNAMENT['Players'] = self.players
        Tournament.TOURNAMENT['Nb rounds'] = self.nb_rounds
        Tournament.TOURNAMENT['Nb tours'] = self.nb_tours
        Tournament.TOURNAMENT['Time control'] = self.time_control
        Tournament.TOURNAMENT['Description'] = self.description

        data_base.DB_ALL_TOURNAMENTS.insert(Tournament.TOURNAMENT)

    @classmethod
    def create_tournament(cls):

        print(f"\n\n{'#' * 119}"
              f"\n| Add a tournament |",
              f"\n{'####################'}\n")

        Tournament(name_tournament=input("Name tournament : "),
                   location=input("Location : "),
                   date=input("Date : "),
                   players=input("Players : "),
                   nb_rounds=int(input("Nb rounds : ")),
                   nb_tours=input("Nb tours : "),
                   time_control=input("Time control : "),
                   description=input("Description : "))

    @classmethod
    def show_tournament(cls):
        print(f"\n\n{'#' * 200}"
              f"\n| Show all tournament |"
              f"\n{'#######################'}\n\n"
              f"{'N°'.center(5)} | " 
              f"{'Name'.center(15)} | "
              f"{'Location'.center(15)} | "
              f"{'Date'.center(10)} | "
              f"{'Players'.center(30)} | "
              f"{'Nb rounds'.center(15)} | "
              f"{'Nb tours'.center(15)} | "
              f"{'Time control'.center(15)} | "
              f"{'Description'.center(30)} |"
              f"\n{'*' * 200}")

        for tournament in data_base.DB_ALL_TOURNAMENTS:
            print(f"{str(tournament.doc_id).center(5)} | "
                  f"{tournament['Name'].center(15)} | "
                  f"{tournament['Location'].center(15)} | "
                  f"{tournament['Date'].center(10)} | "
                  f"{tournament['Players'].center(30)} | "
                  f"{tournament['Nb rounds']:^15} | "
                  f"{tournament['Nb tours']:^15} | "
                  f"{tournament['Time control']:^15} | "
                  f"{tournament['Description'].center(30)} | ")

        print(f"\n{'#' * 200}")


if __name__ == "__main__":
    pass
