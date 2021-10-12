#!/usr/bin/env python
import requests, json, pymsgbox
from time import sleep
url = "http://ed-nm.ibnlive.in.com/livescore/json/cross_inen12162016181708.json?callback=match&_=1482055118271"
#while True:
r = requests.get(url)
print dir(r)
#print r.getcode()
#s = r.json()
#print (json.dumps(s, indent=2))
#j = r.json()
#print j
