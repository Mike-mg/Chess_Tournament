#! /usr/bin/env python3
# coding:utf-8

import datetime
import os
import sys


def format_string(get_string: str) -> str:
    """
    Format the input parameter
    """

    return input(f":: {get_string} > ")


def clear_screen():
    """
    Clear the screen
    """

    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('win32'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')


def time_t():
        return datetime.datetime.now().strftime('%d/%m/%Y - %H:%M:%S')


if __name__ == "__main__":
    pass