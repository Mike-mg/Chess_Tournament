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

        for player in models.models_players.deserialized_table_players():

            if player.doc_id in self.players:
                list_round_1.append((player.doc_id, player['Ranking'], player['Points']))

        list_round_1.sort(key=operator.itemgetter(1))

        list_round_1 = list_round_1[:4], list_round_1[4:]

        match_1 = [list_round_1[0][0], list_round_1[1][0]]
        match_2 = [list_round_1[0][1], list_round_1[1][1]]
        match_3 = [list_round_1[0][2], list_round_1[1][2]]
        match_4 = [list_round_1[0][3], list_round_1[1][3]]

        round_1_dict = {'Round_1': list([match_1, match_2, match_3, match_4])}

        print(round_1_dict['Round_1'])
        return round_1_dict

    def round_2(self, list_results_previous_round):

        list_match_round_1 = list()
        list_player_round_2_tried = list()
        list_player_round_2 = list()
        list_match_round_2 = list()
        player_dict_round_2 = list()
        next_round_dict = dict()

        for match in list_results_previous_round:
            list_match_round_1.append((match[0][0], match[1][0]))
            list_player_round_2_tried.extend(match)

        list_player_round_2_tried.sort(key=operator.itemgetter(2, 1), reverse=True)

        for player in list_player_round_2_tried:
            list_player_round_2.append(player[0])

        y = 1
        while len(list_player_round_2) > 0:

            try:

                match_control = list_player_round_2[0], list_player_round_2[y]

                if match_control in list_match_round_1 or \
                        tuple(reversed(match_control)) in list_match_round_1:
                    match_control = list_player_round_2[0], list_player_round_2[y + 1]

                    if match_control not in list_match_round_1 or \
                            tuple(reversed(match_control)) not in list_match_round_1:
                        list_match_round_2.append(match_control)

                        del list_player_round_2[0]
                        del list_player_round_2[y]

                else:

                    list_match_round_2.append(match_control)
                    del list_player_round_2[:y + 1]

            except IndexError:
                break

        print(list_player_round_2_tried)

        for player in models.models_players.deserialized_table_players():

            for match in list_match_round_2:

                if player.doc_id in match:
                    player_dict_round_2.append((player.doc_id, player['Ranking'], player['Points']))

        next_round_dict['Round_2'] = player_dict_round_2
        print(next_round_dict)

        