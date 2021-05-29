#! /usr/bin/env python3
# coding:utf-8

"""
Modules views
Modules Models
"""

import views.view_tournament


def controller_add_tournament():
    """
    Add player control
    """
    tournament = views.view_tournament.ViewAddTournament()
    # tournament.name_tournament()
    # tournament.location_tournament()
    # tournament.date_tournament()
    # tournament.nb_rounds_tournament()
    tournament.tours_tournament()
    # tournament.add_player_tournament()
    # tournament.time_control_tournament()
    # tournament.description_tournament()

    tournament.round_1_tournament(({tournament.players[0]: 0}, {tournament.players[1]: 0}))

    print(f"Name : {tournament.name}\n"
          f"Location : {tournament.location}\n"
          f"Start date : {tournament.start_date}\n"
          f"End date : {tournament.end_date}\n"
          f"Nb rounds : {tournament.nb_rounds}\n"
          f"Tours : {tournament.tours}\n"
          f"Players : {tournament.players}\n"
          f"Time control : {tournament.time_control}\n"
          f"Description : {tournament.description}")

    tournament.results_round_1()

    tournament.round_2_tournament(({tournament.players[1]: 0}, {tournament.players[0]: 0}))

    print(f"Name : {tournament.name}\n"
          f"Location : {tournament.location}\n"
          f"Start date : {tournament.start_date}\n"
          f"End date : {tournament.end_date}\n"
          f"Nb rounds : {tournament.nb_rounds}\n"
          f"Tours : {tournament.tours}\n"
          f"Players : {tournament.players}\n"
          f"Time control : {tournament.time_control}\n"
          f"Description : {tournament.description}")

    tournament.results_round_2()

    print(f"Name : {tournament.name}\n"
          f"Location : {tournament.location}\n"
          f"Start date : {tournament.start_date}\n"
          f"End date : {tournament.end_date}\n"
          f"Nb rounds : {tournament.nb_rounds}\n"
          f"Tours : {tournament.tours}\n"
          f"Players : {tournament.players}\n"
          f"Time control : {tournament.time_control}\n"
          f"Description : {tournament.description}")


    print(f"\n\nResults of tournament\n"
          f"{'-' * 21}")
