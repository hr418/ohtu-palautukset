import requests


class Player:
    def __init__(self, player_data):
        self.name = player_data["name"]
        self.nationality = player_data["nationality"]
        self.assists = player_data["assists"]
        self.goals = player_data["goals"]
        self.team = player_data["team"]
        self.games = player_data["games"]

    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals} + {self.assists} = {self.goals + self.assists}"


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url, timeout=10).json()
        return [Player(player_dict) for player_dict in response]


class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = [p for p in self.players if p.nationality == nationality]
        filtered_players.sort(key=lambda p: p.goals + p.assists, reverse=True)
        return filtered_players
