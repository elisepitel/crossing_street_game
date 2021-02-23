import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create Player
player = Player()
# link user key action with turtle up movement:
screen.listen()
screen.onkey(player.go_up, 'Up')


car_manager = CarManager()

# Create first set of cars
first_cars = 25
for car in range(first_cars):
    car_manager.create_car()
    car_manager.move_cars()

# Create scoreboard
scoreboard = Scoreboard()
score = 0

game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect if player reach the finish line
    if player.is_at_finish_line():
        player.go_to_start()
        score += 1
        scoreboard.update_scoreboard(score)
        car_manager.level_up()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
