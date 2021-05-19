#! /usr/bin/env python3
# coding:utf-8

import os
import sys

import controllers.controller_menu


class ShowMenu:

    @staticmethod
    def menu():

        if sys.platform.startswith('linux'):
            os.system('clear')
        elif sys.platform.startswith('win32'):
            os.system('cls')
        elif sys.platform.startswith('darwin'):
            os.system('clear')

        menu_list = ['List of all players',
                     'Add a player',
                     'Modified ranking player',
                     'Remove a player',
                     'List of all tournaments',
                     'Add a tournament',
                     'Modified a tournaments',
                     'Return menu',
                     'Leave -*- CHESS TOURNAMENT -*-'
                     ]

        ShowMenu.sub_menu('*** -*- WELCOME TO THE CHESS TOURNAMENT PROGRAM -*- ***')
        ShowMenu.sub_menu('* MENU *')

        for index, m_menu in enumerate(menu_list):
            print(f"{':: '}{index} > {m_menu}")

        print(f"{'-' * 119}")

    @staticmethod
    def choice_menu():

        while 1:

            choice = input(f"\n\n\n{'=' * 22}\n"
                           f"Help : 7 > Return menu"
                           f"\n{'-' * 22}"
                           f"\n{':: Select a option > '}")

            try:
                choice = int(choice)

            except ValueError:
                print(f"\n{':: ERROR > Enter a valid option [0-8]'}\n")
                continue

            controllers.controller_menu.ChoiceMenu.choice_user_menu(choice)

    @staticmethod
    def sub_menu(title):
        print(f"\n\n\n{'=' * 119}\n"
              f"{title.center(119)}\n"
              f"{str('-' * len(title)).center(119)}\n\n")

    @staticmethod
    def get_string_value(get_string):
        return input(f"- {get_string}: ")
