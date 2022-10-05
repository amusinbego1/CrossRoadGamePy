STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.goto(STARTING_POSITION)

    def movef(self):
        self.forward(MOVE_DISTANCE)

    def moveb(self):
        if self.ycor() > -FINISH_LINE_Y:
            self.backward(MOVE_DISTANCE)

    def is_levelup(self):
        return self.ycor() > FINISH_LINE_Y

    def start_pos(self):
        self.goto(STARTING_POSITION)
