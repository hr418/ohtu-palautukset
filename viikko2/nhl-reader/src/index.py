import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == "FIN":
            players.append(player)

    players.sort(key=lambda p: p.goals + p.assists, reverse=True)

    print("Players from FIN:")

    for player in players:
        print(
            f"{player.name:20} {player.team:15} {player.goals} + {player.assists} = {player.goals + player.assists}"
        )


if __name__ == "__main__":
    main()
