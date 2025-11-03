import sys
import os
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54),  # 45+54 = 99
            Player("Kurri", "EDM", 37, 53),  # 37+53 = 90
            Player("Yzerman", "DET", 42, 56),  # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89),  # 35+89 = 124
        ]


@pytest.fixture
def stats():
    s = StatisticsService()
    s._players = PlayerReaderStub().get_players()
    return s


def test_search_returns_player_when_name_matches(stats):
    player = stats.search("Semenko")
    assert player is not None
    assert player.name == "Semenko"

    player2 = stats.search("Semen")
    assert player2 is not None
    assert player2.name == "Semenko"


def test_search_returns_none_when_no_match(stats):
    assert stats.search("Nobody") is None


def test_team_returns_players_of_given_team(stats):
    edm = stats.team("EDM")
    assert [p.name for p in edm] == ["Semenko", "Kurri", "Gretzky"]


def test_team_returns_empty_list_when_no_players(stats):
    assert stats.team("XYZ") == []


def test_top_with_negative_returns_empty_list(stats):
    assert stats.top(-1) == []


def test_top_returns_correct_number_and_order(stats):
    top0 = stats.top(0)
    assert len(top0) == 1
    assert top0[0].name == "Gretzky"

    top2 = stats.top(2)
    assert [p.name for p in top2] == ["Gretzky", "Lemieux", "Yzerman"]


def test_top_with_too_large_index_raises(stats):
    with pytest.raises(IndexError):
        stats.top(10)


def test_top_sort_by_goals_and_assists():
    # players with different goals and assists to exercise SortBy.GOALS and SortBy.ASSISTS
    p1 = Player("G1", "A", 5, 0)  # goals=5, assists=0, points=5
    p2 = Player("G2", "A", 3, 10)  # goals=3, assists=10, points=13
    p3 = Player("G3", "B", 4, 4)  # goals=4, assists=4, points=8

    s = StatisticsService()
    s._players = [p1, p2, p3]

    # sort by GOALS: G1 (5), G3 (4), G2 (3)
    by_goals = s.top(2, sort_by=SortBy.GOALS)
    assert [p.name for p in by_goals] == ["G1", "G3", "G2"][: len(by_goals)]

    # sort by ASSISTS: G2 (10), G3 (4), G1 (0)
    by_assists = s.top(2, sort_by=SortBy.ASSISTS)
    assert [p.name for p in by_assists] == ["G2", "G3", "G1"][: len(by_assists)]
