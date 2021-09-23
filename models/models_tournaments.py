#! /usr/bin/env python3
# coding:utf-8

import operator

import models
import utils
import bdd
import controllers


class Tournament:
    """
    create a object Tournament
    """

    def __init__(
        self,
        name: str,
        location: str,
        start_date: str,
        end_date: str,
        players: list[models.Player],
        time_control: str,
        description: str,
        nb_rounds: int = 4,
        tours: list[dict] = None,
        state: bool = True,
    ):

        self.name = name.title()
        self.location = location.title()
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.time_control = time_control
        self.description = description
        self.nb_rounds = nb_rounds
        self.tours = [] if tours is None else tours
        self.state = state

    def round_1(self) -> None:
        """
        Sort the players and create the matches for round 1
        """

        list_round_1 = list()

        for player in self.players:

            player_dict = bdd.db_functions.TABLE_PLAYERS.get(doc_id=player)

            list_round_1.append((player, player_dict['ranking'], player_dict['points']))

        list_round_1.sort(key=operator.itemgetter(1))

        list_round_1 = list_round_1[:4], list_round_1[4:]

        match_1 = [list_round_1[0][0], list_round_1[1][0]]
        match_2 = [list_round_1[0][1], list_round_1[1][1]]
        match_3 = [list_round_1[0][2], list_round_1[1][2]]
        match_4 = [list_round_1[0][3], list_round_1[1][3]]

        time = utils.time_t()
        round_1_dict = {
            "round_1": [match_1, match_2, match_3, match_4],
            "start_time": time,
            "end_time": str(),
        }

        self.tours.append(round_1_dict)

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

        for key_dict_round, value in self.tours[round_indicator].items():
            # Retrieve the current round

            if key_dict_round == "end_time":
                time = utils.time_t()
                self.tours[round_indicator]["end_time"] = time

            if key_dict_round == f"round_{len(self.tours)}":

                for match in value:
                    # Retrieve the players from each match
                    list_match_round_1.extend(match)

        print(list_match_round_1)

        list_match_round_1.sort(key=operator.itemgetter(2, 1), reverse=True)
        # sort the players by points and then rank

        y = 1
        while len(list_match_round_1) > 0:
            # Check if the players have already played together

            try:

                match = [list_match_round_1[0], list_match_round_1[y]]
                match_control = [match[0][0], match[1][0]]

                if (
                    match_control in list_match_round_1
                    or tuple(reversed(match_control)) in list_match_round_1
                ):

                    match_control = (
                        list_match_round_1[0][0],
                        list_match_round_1[y + 1][0],
                    )

                    if (
                        match_control not in list_match_round_1
                        or tuple(reversed(match_control)) not in list_match_round_1
                    ):
                        list_match_next_round.append(match)

                        del list_match_round_1[0]
                        del list_match_round_1[y]

                else:
                    # Add the match for the next round
                    list_match_next_round.append(match)
                    del list_match_round_1[: y + 1]

            except IndexError:
                break

        time = utils.time_t()

        if len(self.tours) < self.nb_rounds:

            next_round_dict = {
                f"{'round_'}{len(self.tours) + 1}": list_match_next_round,
                "start_time": time,
                "end_time": str(),
            }

            self.tours.append(next_round_dict)
