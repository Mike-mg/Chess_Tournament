#! /usr/bin/env python3
# coding:utf-8

"""
Module view
"""
import views.view_menu
import views.view_tournament


class Main:

    def __init__(self):

        self.menu = views.view_menu.ViewMenu()

    def main(self):
        """
        Enter point
        """

        self.menu.show_menu()
        self.menu.choice_menu()


if __name__ == "__main__":
    main = Main()
    main.main()