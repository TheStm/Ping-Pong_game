from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.left(45)
        self.penup()
        self.x_move = 8
        self.y_move = 8
        self.speed_move = 0.08

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_vertically(self):
        self.y_move *= -1

    def bounce_horizontally(self):
        self.speed_move *= 0.85
        self.x_move *= -1

    def restart(self):
        self.goto(0, 0)
        self.speed_move = 0.08
        self.x_move *= -1
        self.y_move *= -1