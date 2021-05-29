#! /usr/bin/env python3
# coding:utf-8

"""
Module view
"""
import views.view_menu
import views.view_tournament


def main():
    """
    Enter point
    """

    views.view_menu.show_menu()
    views.view_menu.choice_menu()


if __name__ == "__main__":
    main()
