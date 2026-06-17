class Team:

    def __init__(self, name):
        self.name = name
        self.runs_scored = 0
        self.games = 0
        self.wins = 0
        self.losses = 0

    def add_game(self, runs):
        self.runs_scored += runs
        self.games += 1

    def add_win(self):
        self.wins += 1

    def add_loss(self):
        self.losses += 1

    def avg_runs(self):
        if self.games == 0:
            return 0
        return self.runs_scored / self.games

    def win_pct(self):
        total = self.wins + self.losses
        if total == 0:
            return 0
        return self.wins / total
import requests

API_KEY = "YOUR_API_KEY"

headers = {
    "Authorization": API_KEY
}

url = "https://mlb.balldontlie.io/"

response = requests.get(url, headers=headers)

data = response.json()

existing_ids = set()

teams = {}
if team_name not in teams:
    teams[team_name] = Team(team_name)
    teams[home].add_game(home_score)
    teams[away].add_game(away_score)
if home_score > away_score:
    teams[home].add_win()
    teams[away].add_loss()
else:
    teams[away].add_win()
    teams[home].add_loss()

highest_team = max(
    teams.values(),
    key=lambda t: t.avg_runs()
)
lowest_team = min(
    teams.values(),
    key=lambda t: t.avg_runs()
)
best_team = max(
    teams.values(),
    key=lambda t: t.win_pct()
)
worst_team = min(
    teams.values(),
    key=lambda t: t.win_pct()
)
league_avg = sum(
    t.avg_runs() for t in teams.values()
) / len(teams)

import json

with open("results.json", "w") as outfile:
    json.dump(results, outfile, indent=4)