from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console
from player import PlayerReader, PlayerStats


def make_table(title, players):
    table = Table(title=title)
    table.add_column("Released", justify="left", style="cyan")
    table.add_column("teams", justify="left", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.goals + player.assists),
        )
    return table


def main():

    season = Prompt.ask(
        "Season",
        default="2024-25",
        choices=[
            "2018-19",
            "2019-20",
            "2020-21",
            "2021-22",
            "2022-23",
            "2023-24",
            "2024-25",
            "2025-26",
        ],
    )

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = Prompt.ask(
            "Nationality",
            choices=[
                "USA",
                "FIN",
                "CAN",
                "SWE",
                "RUS",
                "CZE",
                "SLO",
                "FRA",
                "GBR",
                "SVK",
                "DEN",
                "NED",
                "AUT",
                "BLR",
                "GER",
                "SUI",
                "NOR",
                "UZB",
                "LAT",
                "AUS",
            ],
        )

        top_players = stats.top_scorers_by_nationality(nationality)

        console = Console()
        console.print(
            make_table(f"Season {season} players from {nationality}", top_players)
        )


if __name__ == "__main__":
    main()
