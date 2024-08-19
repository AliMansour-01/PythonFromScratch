from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.score_keeper()
        self.hideturtle()
    def score_keeper(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    def update_score(self):
        self.clear()
        self.score += 1
        self.score_keeper()
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
