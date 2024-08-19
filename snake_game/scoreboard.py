from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.score_keeper()
        self.hideturtle()
    def score_keeper(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    def update_score(self):
        self.score += 1
        self.score_keeper()
    def reset(self):
        if self.score > self.high_score:
            self.score = self.high_score
        self.score = 0
        self.update_score()