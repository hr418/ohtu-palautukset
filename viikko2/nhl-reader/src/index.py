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

    print("Players from FIN:")

    for player in players:
        print(
            f"{player.name} team {player.team} goals {player.goals} assists {player.assists}"
        )


if __name__ == "__main__":
    main()
