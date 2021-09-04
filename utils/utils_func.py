#! /usr/bin/env python3
# coding:utf-8

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
