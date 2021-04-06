#! /usr/bin/bash
# coding:utf-8


class Player:

    def __init__(self, last_name, name, birthday, sex, ranking):
        self.last_name = last_name
        self.name = name
        self.birthday = birthday
        self.sex = sex
        self.ranking = ranking

    def show_player(self):
        print(f"Full name : {self.last_name} {self.name}, born on : {self.birthday}, sex : {self.sex}, ranking : {self.ranking}")


class Tournament:

    def __init__(self, name_tournament, location, date, tours, players, time_control, description, nb_round=4):
        self.name = name_tournament
        self.location = location
        self.date = date
        self.nb_round = nb_round
        self.tours = tours
        self.players = players
        self.time_control = time_control
        self.description = description

    def show_info_tournament(self):
        print(f"\nTournament information :\n\
        \r------------------------\n\
        \rName          : {self.name}\n\
        \rLocation      : {self.location}\n\
        \rDate          : {self.date}\n\
        \rNb rounds     : {self.nb_round}\n\
        \rTours         : {self.tours}\n\
        \rPlayers       : {self.players}\n\
        \rTime control  : {self.time_control}\n\
        \rDescription   : {self.description}")


def main():
    print("creation of a tournament :\n\
          \r##########################")
    tournament = Tournament(input("Name : "), input("Location : "), input("Date : "), input("Tours : "), input("Players : "), input("Time control : "), input("Description : "))
    tournament.show_info_tournament()

    # print(f"\nPlayer registration :\n\
    # \r#####################\n")
    #
    # for i in range(1, 9):
    #
    #     i = "player " + str(i)
    #     print(f"# {i} :\n\
    #     \r------------")
    #
    #     i = Player(input("Last name : "), input("Name : "), input("Birthday : "), input("Sex : "), input("Ranking : "))
    #     i.show_player()


if __name__ == "__main__":
    main()
