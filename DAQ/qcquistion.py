# -*- coding: utf-8 -*-
from API.opendota import OpenDotA
playerid = 193116840

api = OpenDotA()
# 采集比赛的matchid
matchid_list = api.get_all_matchid()
