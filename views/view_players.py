#! /usr/bin/env python3
# coding:utf-8

import datetime


class ViewAddPlayer:

    def __init__(self):
        self.last_name = f"{input('Last_name : ').capitalize()}"
        self.name = f"{input('Name : ').capitalize()}"
        print("Entrer la date de naissance")
        self.birthday = datetime.date(int(input("annee : ")), int(input("mois : ")), int(input("jour : ")))
        self.sex = f"{input('Sex : ').capitalize()}"
        self.ranking = f"{input('Ranking : ')}"

    @classmethod
    def error_ranking(cls):
        print("\nUne erreur c'est produite, veuillez renseignez un nombre pour le rang du joueur.\n")


if __name__ == "__main__":
    pass

# models.models.Player("Dupont", "Nicolas", "13/07/72", "M", 0)
