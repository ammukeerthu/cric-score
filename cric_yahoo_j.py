#!/usr/bin/env python
import requests, json, pymsgbox
from time import sleep
url = "https://cricket.yahoo.com/ws/score/scorecard.php?content=f5&match_id=194544&media=1&region=IN"
while True:
	r = requests.get(url)
	j = r.json()
	run = j["scorecard"]["s"]["a"]["r"]
	wicket = j["scorecard"]["s"]["a"]["w"]
	score = str(run) + "/" + str(wicket)
	pymsgbox.alert(json.dumps(score, indent=2), title="Live Score!!")
	#print (json.dumps(score, indent=2))
	sleep(60)