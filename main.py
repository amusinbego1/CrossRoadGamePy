import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

leonardo = Player()
screen.listen()
screen.onkey(leonardo.movef, "Up")
screen.onkey(leonardo.moveb, "Down")
garage = CarManager()

game_is_on = True
speed = 0.1
brojac = 0
score = Scoreboard()
score.scrivere(f"Level: {score.level}")

while game_is_on:
    if not garage.move_cars(leonardo.position()):
        game_is_on = False
    time.sleep(speed)
    screen.update()
    garage.del_cars()
    if brojac % 10 == 0:
        garage.add_car()
    if leonardo.is_levelup():
        score.level += 1
        score.scrivere(f"Level: {score.level}")
        leonardo.start_pos()
        garage.start_pos()
        garage = CarManager()
        speed *= 0.7
    brojac += 1

gameover = Scoreboard()
gameover.goto(0, 0)
gameover.scrivere("GAME OVER")

screen.exitonclick()