#! /usr/bin/env python3
# coding:utf-8

from tinydb import TinyDB
import operator

import bdd

DB_TOURNAMENTS = TinyDB('bdd/db_tournaments.json', indent=4)
TOURNAMENTS = DB_TOURNAMENTS.table("tournaments")


class Tournament:
    """
    create a object Tournament
    """

    def __init__(self, name: str,
                 location: str,
                 start_date: str,
                 end_date: str,
                 players: list[int],
                 time_control: str,
                 description: str):

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
        """
        Sort the players and create the matches for round 1
        """

        list_round_1 = list()

        for id_player, player in enumerate(bdd.deserialized_table_players()):

            if id_player in self.players:

                list_round_1.append((id_player, player.ranking, player.points))

        list_round_1.sort(key=operator.itemgetter(1))

        list_round_1 = list_round_1[:4], list_round_1[4:]

        match_1 = [list_round_1[0][0], list_round_1[1][0]]
        match_2 = [list_round_1[0][1], list_round_1[1][1]]
        match_3 = [list_round_1[0][2], list_round_1[1][2]]
        match_4 = [list_round_1[0][3], list_round_1[1][3]]

        round_1_dict = {'Round_1': [match_1, match_2, match_3, match_4]}

        self.tours.insert(0, round_1_dict)

    def next_round(self):
        """
        - Retrieve the current round
        - Sort the matches by the number of points of the players
        - Check if the players have already played together
        - Create the next round
        """

        for round_actual in self.tours[-1].values():
            # Retrieve the current round

            list_match_round_1 = list()
            list_player_next_round_tried = list()
            list_match_next_round = list()

            for match in round_actual:
                # Retrieve the players from each match

                list_match_round_1.append((match[0][0], match[1][0]))
                list_player_next_round_tried.extend(match)

            list_player_next_round_tried.sort(key=operator.itemgetter(2, 1), reverse=True)
            # sort the players by points and then rank

            y = 1
            while len(list_player_next_round_tried) > 0:
                # Check if the players have already played together

                try:

                    match = [list_player_next_round_tried[0], list_player_next_round_tried[y]]
                    match_control = [match[0][0], match[1][0]]

                    if match_control in list_match_round_1 or tuple(reversed(match_control)) in list_match_round_1:

                        match_control = list_player_next_round_tried[0][0], list_player_next_round_tried[y + 1][0]

                        if match_control not in list_match_round_1 or tuple(
                                reversed(match_control)) not in list_match_round_1:
                            list_match_next_round.append(match)

                            del list_player_next_round_tried[0]
                            del list_player_next_round_tried[y]

                    else:
                        # Add the match for the next round
                        list_match_next_round.append(match)
                        del list_player_next_round_tried[:y + 1]

                except IndexError:
                    break

            if len(self.tours) < self.nb_rounds:
                next_round_dict = {f"{'Round_'}{len(self.tours)+1}": list_match_next_round}
                self.tours.insert(len(self.tours), next_round_dict)

            else:
                print("\n\nThe tournament is finnish.")
