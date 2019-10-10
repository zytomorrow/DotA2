# -*- coding: utf-8 -*-

import sqlite3
import os


class Data(object):
    def __init__(self):
        print(os.getcwd())
        self.db = sqlite3.connect("./DATA.db")
        self.cur = self.db.cursor()
        with open("./DB/init.sql", encoding="UTF8") as sqlscript:
            self.cur.executescript(str(sqlscript.read()))

    def insert_player_info(self, **player_info):
        self.cur.execute(f"INSERT INTO players {tuple(player_info.keys())} VALUES {tuple(player_info.values())};")

    def insert_match_details(self, **detail):
        self.cur.execute(f"INSERT INTO")

    def __del__(self):
        self.db.commit()
        self.cur.close()
        self.db.close()


db = Data()

info = {"steamid": "sad",
        "communityvisibilitystate": 1
        }

db.insert_player_info(**info)
