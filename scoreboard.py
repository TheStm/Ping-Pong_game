from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.r_score = -1
        self.l_score = -1
        self.increase_r_score()
        self.increase_l_score()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.write(f"{self.l_score}     {self.r_score}", False, align="center", font=("Courier", 80, "normal"))

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.l_score}     {self.r_score}", False, align="center", font=("Courier", 80, "normal"))