import requests, easygui
from time import sleep
from bs4 import BeautifulSoup
url = "http://m.cricbuzz.com/cricket-commentary/16872/ind-vs-eng-5th-test-england-tour-of-india-2016-17" 
while True:
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	data=soup.find("span",{"class":"miniscore-teams ui-bat-team-scores"}).getText()
	data2=soup.find("span",{"class":"crr"}).getText()
	message = ""
	message = data + "\n" + data2
	easygui.msgbox(message, title="Live Score")
	sleep(60)	