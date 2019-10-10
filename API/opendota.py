# -*- coding: utf-8 -*-
"""
目前没有找到合适的API接入。
opendota的官方API是收费的，免费的又请求次数限制
opendota的web端的API请求是没有做反爬的，所以集成成API
"""

from pprint import pprint
from requests import Session
import json


class OpenDotA(object):
    def __init__(self):
        self.main_url = "https://api.opendota.com/api"
        self.session = Session()

    def get_all_matchid(self, playerid):
        """
        指定玩家数字ID，获取所有的比赛id
        """
        res = self.session.get(f"{self.main_url}/players/{playerid}/matches?significant=0")
        return [item["match_id"] for item in json.loads(res.content.decode())]

    def get_player_winlose(self, playerid):
        """
        指定玩家数字ID，获取总胜负场次
        """
        res = self.session.get(f"{self.main_url}/players/{playerid}/wl?")
        return json.loads(res.content.decode())

    def get_match_details(self, matchid):
        """
        指定比赛id，获取该场比赛的详情
        """
        res = self.session.get(f"{self.main_url}/matches/{matchid}?")
        return json.loads(res.content.decode())

    def get_all_items(self):
        """
        获取所有的游戏物品
        """
        res = self.session.get(f"{self.main_url}/")

    def get_heros_info(self, uid):
        """
        获取玩家的全英雄统计
        """
        res = self.session.get(f"{self.main_url}/players/{uid}/heroes?")
        return json.loads(res.content.decode())

    def player_counts(self, uid):
        """
        获取玩家游戏匹配统计
        """


if __name__ == "__main__":
    api = OpenDotA()
    players = 193116840
    # print(api.get_all_matchid(players))
    # print(api.get_player_winlose(players)
    # pprint(api.get_match_details(1360329099))
    pprint(api.get_heros_info(1360329099))
    # x = api.get_match_details(1360329099).keys()

    # for i in x:
    # print(i)
