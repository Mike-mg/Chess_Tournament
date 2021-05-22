#! /usr/bin/env python3
# coding:utf-8

import os
import sys

import controllers.controller_menu


class ShowMenu:
    '''
    Docstrings
    '''

    def __init__(self):

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

        SubMenu('/^\ *** -*- WELCOME TO THE CHESS TOURNAMENT PROGRAM -*- *** /^\\')
        SubMenu('* MENU *')

        for index, m_menu in enumerate(menu_list):
            print(f"{':: '}{index} > {m_menu}")

        print(f"{'-' * 119}")


class ChoiceMenu():
    '''
    Docstrings
    '''

    def __init__(self):

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


class SubMenu:
    '''
    Docstrings
    '''

    def __init__(self,title):

        print(f"\n\n\n{'=' * 119}\n"
              f"{title.center(119)}\n"
              f"{str('-' * len(title)).center(119)}\n\n")
