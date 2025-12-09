class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    DEUCE_THRESHOLD = 3
    WIN_THRESHOLD = 4

    SCORE_NAMES = {LOVE: "Love", FIFTEEN: "Fifteen", THIRTY: "Thirty", FORTY: "Forty"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._get_tied_score()
        elif (
            self.player1_score >= self.WIN_THRESHOLD
            or self.player2_score >= self.WIN_THRESHOLD
        ):
            return self._get_endgame_score()
        else:
            return self._get_regular_score()

    def _get_tied_score(self):
        if self.player1_score < self.DEUCE_THRESHOLD:
            return f"{self.SCORE_NAMES[self.player1_score]}-All"
        return "Deuce"

    def _get_endgame_score(self):
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def _get_regular_score(self):
        player1_score_name = self.SCORE_NAMES[self.player1_score]
        player2_score_name = self.SCORE_NAMES[self.player2_score]
        return f"{player1_score_name}-{player2_score_name}"
