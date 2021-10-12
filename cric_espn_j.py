#!/usr/bin/env python
import requests, json, pymsgbox
from time import sleep
url = "http://www.espncricinfo.com/netstorage/1034817.json?xhr=1"
while True:
	r = requests.get(url)
	j = r.json()
	score = j["live"]["fow"][0]["fow_runs"]
	x = json.dumps(score, indent=2)
	wicket = j["live"]["fow"][0]["fow_wickets"]
	y = json.dumps(wicket, indent=2)
	live = "Score: " + x + "/" + y
	pymsgbox.alert(live, title="Live Updates!!")
	sleep(02)