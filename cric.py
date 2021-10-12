#!/usr/bin/env python
import requests, json, easygui, sys
from time import sleep
from gi.repository import Notify
Notify.init("Test App")

def print_score(url):
    try:
        while True:
            r = requests.get(url)
            j = r.json()

            series = j["series"]["name"]
            status = j["status"]

            batting_team_score = j["score"]["batting"]["score"]
            bowling_team_score = j["score"]["bowling"]["score"]

            rr     = j["score"]["rrr"]
            target = j["score"]["target"]

            batting_team_id = j["score"]["batting"]["id"]
            batsman1_id     = j["score"]["batsman"][0]["id"]                        
            batsman1_runs   = j["score"]["batsman"][0]["r"]
            batsman1_balls  = j["score"]["batsman"][0]["b"]
            batsman2_id     = j["score"]["batsman"][1]["id"]                        
            batsman2_runs   = j["score"]["batsman"][1]["r"]
            batsman2_balls  = j["score"]["batsman"][1]["b"]

            bowler_id     = j["score"]["bowler"][0]["id"]
            bowler_runs   = j["score"]["bowler"][0]["r"]
            bowler_overs  = j["score"]["bowler"][0]["o"]
            bowler_wkts   = j["score"]["bowler"][0]["w"]

            if j["score"]["batsman"][0]["strike"] == 1:
                batsman_on_strike = batsman1_id
            else:
                batsman_on_strike = batsman2_id

            if batting_team_id == j["team1"]["id"]:
                batting_team = j["team1"]["name"]
                bowling_team = j["team2"]["name"]
            else:
                batting_team = j["team2"]["name"]
                bowling_team = j["team1"]["name"]

            for player in j["players"]:
                 if batsman1_id == player["id"]:
                     if batsman1_id == batsman_on_strike:
                         batsman1_name = player["f_name"] + "*"
                     else:
                         batsman1_name = player["f_name"]
                 elif batsman2_id == player["id"]:
                     if batsman2_id == batsman_on_strike:
                         batsman2_name = player["f_name"] + "*"
                     else:
                         batsman2_name = player["f_name"]
                 elif bowler_id == player["id"]:
                     bowler_name = player["f_name"]

            display_content = """\
            Series : %s
            %s : %s \t %s : %s \t Runrate : %s 
            Target : %s \t Status: %s
            Batsmen: 
               %s : %s (%s)
               %s : %s (%s)
            Bowler:
               %s : %s - %s (%s)
            """ % (series, bowling_team, bowling_team_score, batting_team, batting_team_score, rr, target, status, batsman1_name, batsman1_runs, batsman1_balls, batsman2_name, batsman2_runs, batsman2_balls, bowler_name, bowler_runs, bowler_wkts, bowler_overs)
            title = "Live Score Updates: " + batting_team_score + "vs" + bowling_team
			
            Notify.Notification.new(
                "Ding!",
                display_content,
                "/home/KEERTHANA/cricket_score/cb.jpg"
            ).show()

            sleep(60)
    except requests.ConnectionError as e:
        print(e.__class__.__name__)
        print(str(e))

def print_usage():
    print "Usage: " + sys.argv[1] + "match_id"

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print_usage()
    else:
        url = "https://push.cricbuzz.com/match-api/" + sys.argv[1] + "/commentary.json"
        print url
        print_score(url)
