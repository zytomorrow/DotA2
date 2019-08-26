# -*- coding: utf-8 -*-


"""
目前没有找到合适的API接入。
opendota的官方API是收费的，免费的又请求次数限制
opendota的web端的API请求是没有做反爬的，所以集成成API
"""

from requests import Session
import json


class OpenDotA(object):
    def __init__(self):
        self.main_url = "https://api.opendota.com/api"
        self.session = Session()

    def get_all_matchid(self, playerid):
        res = self.session.get(
            f"{self.main_url}/players/{playerid}/matches?significant=0")
        return [item["match_id"] for item in json.loads(res.content.decode())]

    def get_player_winlose(self, playerid):
        res = self.session.get(f"{self.main_url}/players/{playerid}/wl?")
        return json.loads(res.content.decode())

    def get_match_details(self, matchid):
        res = self.session.get(f"{self.main_url}/matches/{matchid}?")
        return json.loads(res.content.decode())


if __name__ == "__main__":
    api = OpenDotA()
    players = 193116840
    # print(api.get_all_matchid(players))
    # print(api.get_player_winlose(players))
    # print(api.get_match_details(1360329099).keys())

    x = api.get_match_details(1360329099).keys()

    for i in x:
        print(i)
