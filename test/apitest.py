# -*- coding: utf-8 -*-

import requests


print(requests.get("https://api.opendota.com/api/players/193116840/matches?significant=0").json())