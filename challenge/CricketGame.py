import random


class Game:

    matchChar = [1, 2, 3, 4, 0, 6, "bold", "catch out", "run out"]
    random.shuffle(matchChar)

    t1_score = 0
    t2_score = 0
    t1_wicket = 0
    t2_wicket = 0

    def __init__(self, team, team_list):
        self.team1 = team
        self.team1_list = team_list
        self.team2 = "computer"
        self.team2_list = ["p1", "p2", "p3", "p4", "p5"]

    def start_game(self):

        w1 = self.t1_wicket
        w2 = self.t2_wicket
        curr_ball = 0

        while curr_ball < 12 and w1 < 5 and w2 < 5:
            team1_action = random.choice(self.matchChar)
            team2_action = random.choice(self.matchChar)
            self.match_status(team1_action, team2_action)
            print()

            w1 = self.t1_wicket
            w2 = self.t2_wicket
            curr_ball += 1

        self.match_winner(self.t1_score, self.t2_score)
        print(
            f"{self.team1} team remaining wicket "
            f"{self.team1_list[self.t1_wicket :]}"
        )
        print(
            f"{self.team2} team remaining wicket" f"{self.team2_list[self.t2_wicket :]}"
        )

    def match_status(self, team1_action, team2_action):

        if isinstance(team1_action, int):
            self.t1_score += team1_action
            print(
                f"{self.team1} score is {self.t1_score} and wicket is {self.t1_wicket}"
            )
        if isinstance(team1_action, str):
            self.t1_wicket += 1
            print(
                f"{self.team1} score is {self.t1_score} and wicket is {self.t1_wicket}"
            )
        if isinstance(team2_action, int):
            self.t2_score += team2_action
            print(
                f"{self.team2} score is {self.t2_score} and wicket is {self.t2_wicket}"
            )
        if isinstance(team2_action, str):
            self.t2_wicket += 1
            print(
                f"{self.team2} score is {self.t2_score} and wicket is {self.t2_wicket}"
            )

    def match_winner(self, t1_score, t2_score):

        if t1_score > t2_score:
            print(f"team {self.team1} is winner with {t1_score - t2_score} run")
        elif t2_score > t1_score:
            print(f"team {self.team2} is winner with {t2_score - t1_score} run")
        else:
            print(f"match is tai with {t1_score}")


# passing team captain name with team list
game = Game("anurodh", ["a1", "a2", "a3", "a4", "a5"])
game.start_game()
