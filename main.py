#! /usr/bin/env python3
# coding:utf-8

import controllers.controller_menu


class Main:
    """
    Program entry point
    """

    def __init__(self):

        self.menu = controllers.controller_menu.ControllerMenu()

    def start_main(self):
        """
        Show the menu while var choice_user_menu is True (7 = False and quit the program)
        """

        self.menu.show_menu()

        while True:

            if self.menu.choice_user_menu() is False:
                break


if __name__ == "__main__":
    main = Main()
    main.start_main()
