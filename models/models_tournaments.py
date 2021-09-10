#! /usr/bin/env python3
# coding:utf-8

import datetime
import operator

import models


class Tournament:
    """
    create a object Tournament
    """

    def __init__(self, name: str,
                 location: str,
                 start_date: str,
                 end_date: str,
                 players: list[models.Player],
                 time_control: str,
                 description: str,
                 nb_rounds: int = 4,
                 tours: list[dict] = []):

        self.name = name.title()
        self.location = location.title()
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.time_control = time_control
        self.description = description
        self.nb_rounds = nb_rounds
        self.tours = tours

    def round_1(self) -> tuple:
        """
        Sort the players and create the matches for round 1
        """

        list_round_1 = list()

        for id_player, player in enumerate(self.players):

            list_round_1.append((id_player, player.ranking, player.points))

        list_round_1.sort(key=operator.itemgetter(1))

        list_round_1 = list_round_1[:4], list_round_1[4:]

        match_1 = [list_round_1[0][0], list_round_1[1][0]]
        match_2 = [list_round_1[0][1], list_round_1[1][1]]
        match_3 = [list_round_1[0][2], list_round_1[1][2]]
        match_4 = [list_round_1[0][3], list_round_1[1][3]]

        round_1_dict = {'Round_1': [match_1, match_2, match_3, match_4],
                        'Start_time': datetime.datetime.now().strftime('%d/%m/%Y - %H:%M'), 'End_time': str()}

        return len(self.tours), round_1_dict

    def next_round(self):
        """
        - Retrieve the current round
        - Sort the matches by the number of points of the players
        - Check if the players have already played together
        - Create the next round
        """

        round_indicator = len(self.tours) - 1
        list_match_round_1 = list()
        list_match_next_round = list()

        for round_actual in self.tours[round_indicator][f"Round_{len(self.tours)}"]:
            # Retrieve the current round

            for match in round_actual:
                # Retrieve the players from each match
                list_match_round_1.append(match)

        list_match_round_1.sort(key=operator.itemgetter(2, 1), reverse=True)
        # sort the players by points and then rank

        y = 1
        while len(list_match_round_1) > 0:
            # Check if the players have already played together

            try:

                match = [list_match_round_1[0], list_match_round_1[y]]
                match_control = [match[0][0], match[1][0]]

                if match_control in list_match_round_1 or tuple(reversed(match_control)) in list_match_round_1:

                    match_control = list_match_round_1[0][0], list_match_round_1[y + 1][0]

                    if match_control not in list_match_round_1 or tuple(
                            reversed(match_control)) not in list_match_round_1:
                        list_match_next_round.append(match)

                        del list_match_round_1[0]
                        del list_match_round_1[y]

                else:
                    # Add the match for the next round
                    list_match_next_round.append(match)
                    del list_match_round_1[:y + 1]

            except IndexError:
                break

        if len(self.tours) < self.nb_rounds:
            next_round_dict = {f"{'Round_'}{len(self.tours)+1}": list_match_next_round}
            self.tours.insert(len(self.tours), next_round_dict)

        else:
            print("\n\nThe tournament is finnish.")
