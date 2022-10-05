FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-180, 250)


    def scrivere(self, string):
        self.clear()
        self.write(string, False, "center", FONT)
