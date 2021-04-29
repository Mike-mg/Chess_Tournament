#! usr/bin/env python3
# coding:utf-8

"""Docstring"""


from tinydb import TinyDB

DB_PLAYERS = TinyDB('db_players.json', indent=4)
DB_ALL_PLAYERS = DB_PLAYERS.table('players')

DB_TOURNAMENTS = TinyDB('db_tournaments.json', indent=4)
DB_ALL_TOURNAMENTS = DB_TOURNAMENTS.table('tournaments')
