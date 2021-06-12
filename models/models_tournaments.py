#! /usr/bin/env python3
# coding:utf-8

from tinydb import TinyDB
import operator

import models.models_players

DB_TOURNAMENTS = TinyDB('Bdd/db_tournaments.json', indent=4)
TOURNAMENTS = DB_TOURNAMENTS.table("tournaments")


class Tournament:
    """
    create a object Tournament
    """

    def __init__(self, name, location, start_date, end_date,
                 players, time_control, description):

        self.name = name.title()
        self.location = location.title()
        self.start_date = start_date
        self.end_date = end_date
        self.nb_rounds = 4
        self.tours = []
        self.players = players
        self.time_control = time_control
        self.description = description

    def round_1(self):

        list_round_1 = list()

        for k, v in enumerate(models.models_players.deserialized_table_players()):
            if k in self.players:
                list_round_1.append((k, v['Ranking'], v['Points']))

        list_round_1.sort(key=operator.itemgetter(1))

        list_round_1 = list_round_1[:4], list_round_1[4:]

        match_1 = [list_round_1[0][0], list_round_1[1][0]]
        match_2 = [list_round_1[0][1], list_round_1[1][1]]
        match_3 = [list_round_1[0][2], list_round_1[1][2]]
        match_4 = [list_round_1[0][3], list_round_1[1][3]]

        round_1_dict = {'Round_1': list([match_1, match_2, match_3, match_4])}

        return round_1_dict

    def round_2(self, list_results_round_1):

        all_match_round_1 = list()
        list_round_2 = list()

        for match in list_results_round_1:

            for player in match:
                list_round_2.append(player)

        list_round_2.sort(key=operator.itemgetter(2, 1))

        for match in list_results_round_1:
             all_match_round_1.append((match[0][0], match[1][0]))


        if list_round_2 not in all_match_round_1:
            print(all_match_round_1)
            print(list_round_2[:2][0][0], list_round_2[:2][1][0])
            print('le match a deja ete jouer')




            # print('------')
            #
            #
            # for match in list_round_2:
            #     print(match[0][0],match[1][0])
            # print(match[0][0], match[0][1])




        # match_1 = [list_round_2[0][0], list_round_2[0][1]]
        # match_2 = [list_round_2[0][2], list_round_2[0][3]]
        # match_3 = [list_round_2[1][0], list_round_2[1][1]]
        # match_4 = [list_round_2[1][2], list_round_2[1][3]]
        #
        # round_2_dict = {'Round_2': list([match_1, match_2, match_3, match_4])}
        #
        # return round_2_dict