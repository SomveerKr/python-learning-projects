"""
Turtle Crossing Game main module.
Sets up the game window, initializes game objects, and runs the main game loop.
Handles user input and game logic for player movement, car spawning, collision detection, and level progression.
"""
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Create game objects
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

# Set up keyboard controls for player movement
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True

# Main game loop
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Randomly create a new car
    if random.randint(1, 6) == 1:
        car_manager.create_car()
    car_manager.move_cars()
    car_manager.remove_offscreen_cars()

    # Check for collision between player and any car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check if player has reached the finish line
    if player.has_reached_finish_line():
        car_manager.increase_speed()
        player.reset_position()
        scoreboard.increase_level()

# Wait for user to click to exit
screen.exitonclick()