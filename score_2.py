#!/usr/bin/env python
import requests, json, easygui 
from time import sleep

try:
    url = "http://push.cricbuzz.com/match-api/16872/commentary.json"
    while True:
        r = requests.get(url)
        j = r.json()
        score = j["score"]["batting"]["score"]
        easygui.msgbox(json.dumps(score, indent=2), title="Live Score")
        #print json.dumps(score, indent=2)
        sleep(60)
except requests.ConnectionError as e:
    print(e.__class__.__name__)
    print(str(e))
