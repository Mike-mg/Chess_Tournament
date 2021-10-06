#! /usr/bin/env python3
# coding:utf-8

import datetime
import os
import sys

DIRECTORY = ["bdd", "controllers", "main.py", "models", "utils", "views"]


def format_string(get_string: str) -> str:
    """
    Format the input parameter
    """

    return input(f":: {get_string} > ")


def clear_screen() -> None:
    """
    Clear the screen
    """

    if sys.platform.startswith("linux"):
        os.system("clear")
    elif sys.platform.startswith("win32"):
        os.system("cls")
    elif sys.platform.startswith("darwin"):
        os.system("clear")


def time_t() -> str:
    """
    get time
    """
    return datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")


def report_flake8_html() -> None:
    """
    Save all reports in flake8-report
    """

    for path in DIRECTORY:
        os.system(f"flake8 {path} --format=html --htmldir=flake-report/reports_{path}")


if __name__ == "__main__":
    pass
