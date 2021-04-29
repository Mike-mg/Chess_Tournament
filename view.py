#! usr/bin/env python3
# coding:utf-8

import os
import sys


class ShowMenu:
    """
    Menu of program
    """

    @classmethod
    def menu(cls):

        if sys.platform.startswith('linux'):
            os.system('clear')
        elif sys.platform.startswith('win32'):
            os.system('cls')
        elif sys.platform.startswith('darwin'):
            os.system('clear')

        menu_list = ['Add a player',
                     'Show all players',
                     'Create a tournament',
                     'Show all tournaments',
                     'Check current tournaments',
                     'Leave the tournament']

        print(f"\n{'#' * 119}")

        for index, m_menu in enumerate(menu_list):
            print(f"{'#'}{str(index).center(5)}> {m_menu:109}", f"{'#'}")

        print(f"{'#' * 119}")
