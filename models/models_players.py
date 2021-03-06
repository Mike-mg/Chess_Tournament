#! /usr/bin/env python3
# coding:utf-8


class Player:
    """
    Class that creates player objects
    """

    def __init__(
        self,
        last_name: str,
        name: str,
        birthday: str,
        sex: str,
        ranking: int,
        points: int = 0,
        player_id: int = None,
    ):

        self.last_name = last_name.capitalize()
        self.name = name.capitalize()
        self.birthday = birthday
        self.sex = sex.capitalize()
        self.ranking = ranking
        self.points = points
        self.player_id = player_id


if __name__ == "__main__":
    pass
