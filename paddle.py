from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, cord):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setx(cord)

    def go_up(self):
        self.sety(self.ycor() + 20)

    def go_down(self):
        self.sety(self.ycor() - 20)