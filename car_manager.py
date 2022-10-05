COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager():
    def __init__(self):
        self.auta = []

    def add_car(self):
        self.auta.append(Turtle(shape="square"))
        self.auta[len(self.auta)-1].penup()
        self.auta[len(self.auta)-1].shapesize(1, 2)
        self.auta[len(self.auta)-1].color(random.choice(COLORS))
        self.auta[len(self.auta)-1].setheading(180)
        self.y = random.randrange(-280, 280, 25)
        positions = [random.randrange(-280, 280, 25), random.randrange(-280, 280, 25), random.randrange(-280, 280, 25), random.randrange(-280, 280, 25), random.randrange(-280, 280, 25), random.randrange(-280, 280, 25)]
        while self.y in positions:
            self.y = random.randrange(-280, 280, 25)
        positions.append(self.y)
        positions.pop(0)
        self.auta[len(self.auta)-1].goto(random.randint(300, 600), self.y)

    def move_cars(self, lpos):
        for x in self.auta:
            x.forward(5)
            if x.distance(lpos) < 21 or (x.distance(lpos) < 30 and abs(lpos[1] - x.ycor()) < 20):
                return False
        return True

    def del_cars(self):
        r = len(self.auta)
        i = 0
        while i<r:
            r = len(self.auta)
            if self.auta[i].xcor() <= -320:
                self.auta[i].hideturtle()
                self.auta.remove(self.auta[i])
                i -= 1
            i+=1

    def start_pos(self):
        for x in self.auta:
            x.hideturtle()
