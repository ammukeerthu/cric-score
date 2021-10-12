#!/usr/bin/env python
import requests, easygui
from bs4 import BeautifulSoup
from time import sleep
url = "http://www.firstpost.com/cricket-live-score/update-india-v-england-test/2648/181708.html"
while True:
	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')
	#print(soup.encode("utf-8"))
	data1 = soup.find("h1",{"class":"b23cl"}).getText()
	data2 = soup.find("div",{"class":"total clearfix"}).getText()
	data3 = soup.find("p",{"id":"match_status"}).getText()	
	message = data1 + "\n" + data2 + "\n" + data3
	easygui.msgbox(message, title="Live Score!!")
	sleep(60)