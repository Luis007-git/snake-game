from turtle import Turtle

TOPX_SCREEN = 300


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        self.high_score = self.get_high_score()
        super().__init__()
        self.hideturtle()
        self.goto(0, TOPX_SCREEN - 30)
        self.color('Green')
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(0, TOPX_SCREEN - 30)
        self.write(f"CURRENT SCORE: {self.score} High SCORE: {self.high_score}", align='Center')

    def add_point(self):
        self.score += 1
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"game over  {self.score}", align='center')

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score_board()

    def get_high_score(self):
        with open('data.txt') as file:
            self.high_score = int(file.read())
        return self.high_score
