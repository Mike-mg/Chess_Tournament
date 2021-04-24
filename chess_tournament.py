#! /usr/bin/env python3
# coding:utf-8

from tinydb import TinyDB

DB_PLAYERS = TinyDB('db_players.json', indent=4)
DB_ALL_PLAYERS = DB_PLAYERS.table('players')

DB_TOURNAMENTS = TinyDB('db_tournaments.json', indent=4)
DB_ALL_TOURNAMENTS = DB_TOURNAMENTS.table('tournamentS')


class MPlayer:

    PLAYER = {}

    def __init__(self, last_name, name, birthday, sex, ranking):
        self.last_name = last_name.title()
        self.name = name.title()
        self.birthday = birthday
        self.sex = sex.title()
        self.ranking = abs(ranking)

        MPlayer.PLAYER['Last name'] = self.last_name
        MPlayer.PLAYER['Name'] = self.name
        MPlayer.PLAYER['Birthday'] = self.birthday
        MPlayer.PLAYER['Sex'] = self.sex
        MPlayer.PLAYER['Ranking'] = self.ranking

        DB_ALL_PLAYERS.insert(MPlayer.PLAYER)


class Tournament:

    TOURNAMENT = {}

    def __init__(self, name_tournament, location, date, nb_rounds, tours, time_control, description):
        self.name = name_tournament.title()
        self.location = location.title()
        self.date = date
        self.nb_rounds = nb_rounds
        self.tours = tours
        self.time_control = time_control
        self.description = description.title()

        Tournament.TOURNAMENT['Name'] = self.name
        Tournament.TOURNAMENT['Location'] = self.location
        Tournament.TOURNAMENT['Date'] = self.date
        Tournament.TOURNAMENT['Nb_rounds'] = self.nb_rounds
        Tournament.TOURNAMENT['Tours'] = self.tours
        Tournament.TOURNAMENT['Time control'] = self.time_control
        Tournament.TOURNAMENT['Description'] = self.description

        DB_ALL_TOURNAMENTS.insert(Tournament.TOURNAMENT)

    @classmethod
    def show_players(cls):
        print(f"{'*' * 80}\n{'N°'.center(5)} | {'Last name'.center(15)} |",
              f"{'Name'.center(15)} | {'Birthday'.center(15)}",
              f"| {'Sex'.center(5)} | {'Ranking'.center(5)}\n{'*' * 80}")

        for player in DB_ALL_PLAYERS:
            print(f"{str(player.doc_id).center(5)} |"
                  f"{player['Last name'].center(15)} |"
                  f"{player['Name'].center(15)} |"
                  f"{player['Birthday'].center(15)} |"
                  f"{player['Sex'].center(5)} |"
                  f"{str(player['Ranking']).center(5)}")


def main():

    def create_tournament():
        Tournament.show_players()

        print(f"\n\n{'Create a new tournament'}\n"\
              f"{'*' * 80}\n")
        tournament1 = Tournament(f"{input('Name of tournament : ')},"
                                 f"{input('Location : ')},"
                                 f"{input('Date : ')},"
                                 f"{input('Nb rounds : ')},"
                                 f"{input('Nb tours : ')},"
                                 f"{input('Players : ')},"
                                 f"{input('Time control : ')},"
                                 f"{input('Description of tournament : ')},")
    # tournament2 = Tournament("ch1", "toulouse", "220421", 4, 5, 12, "ch2 de toulouse")

    create_tournament()


if __name__ == "__main__":
    main()

    # @property
    # def show_info_tournament(self):
    #     return (f"""\n{'Tournament information :'}
    #     \r{'========================'}\n\
    #     \rName          : {self.name}\n\
    #     \rLocation      : {self.location}\n\
    #     \rDate          : {self.date}\n\
    #     \rNb rounds     : {self.nb_round}\n\
    #     \rTours         : {self.tours}\n\
    #     \rPlayers       : {self.players}\n\
    #     \rTime control  : {self.time_control}\n\
    #     \rDescription   : {self.description}""")

    # player_1 = Player("Dupont", "Nicolas", "13/07/72", "M" ,0)
    # player_2 = Player("Artix", "Emma", "14/01/73", "F", 0)
    # player_3 = Player("Petit", "Angélique", "15/02/74", "F", 0)
    # player_4 = Player("Roux", "Michael", "16/03/75", "M", 0)
    # player_5 = Player("Thiers", "Pierre", "17/04/76", "M", 0)
    # player_6 = Player("Ponthier", "Jade", "18/05/77", "F", 0)
    # player_7 = Player("Rey", "Léo", "19/06/78", "M", 0)
    # player_8 = Player("Fournier", "Manon", "20/07/79", "F", 0)
