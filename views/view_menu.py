#! /usr/bin/env python3
# coding:utf-8

import os
import sys


class ViewMenu:

    def show_menu(self):
        """
        Docstrings
        """

        if sys.platform.startswith('linux'):
            os.system('clear')
        elif sys.platform.startswith('win32'):
            os.system('cls')
        elif sys.platform.startswith('darwin'):
            os.system('clear')

        menu_list = ['List of all players',
                     'Add a player',
                     'Modified ranking player',
                     'List of all tournaments',
                     'Add a tournament',
                     'Modified a tournament',
                     'Return menu',
                     'Leave -*- CHESS TOURNAMENT -*-'
                     ]

        self.sub_menu(r'/^\ *** -*- WELCOME TO THE CHESS TOURNAMENT PROGRAM -*- *** /^\\')
        self.sub_menu('* MENU *')

        for index, m_menu in enumerate(menu_list):
            print(f"[ {index} ]  {m_menu}")

        print(f"{'-' * 119}")

    def choice_menu(self):
        """
        Docstrings
        """

        choice = input(f"\n\n\n{'=' * 22}\n"
                       f"Help : 6 > Return menu"
                       f"\n{'-' * 22}"
                       f"\n{':: Select a option > '}")

        try:
            choice = int(choice)

        except ValueError:
            print(f"\n{':: ERROR > Enter a valid option [0-8]'}\n")

        return choice

    def sub_menu(self, title):
        """
        Docstrings
        """

        print(f"\n\n\n{'=' * 119}\n"
              f"{title.center(119)}\n"
              f"{str('-' * len(title)).center(119)}\n\n")
