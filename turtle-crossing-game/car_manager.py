from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    """
    Manages all car objects in the game, including creation, movement, speed, and removal.
    """
    def __init__(self):
        """
        Initializes the car manager with an empty car list and sets the starting speed.
        """
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        Creates a new car with random color and position, and adds it to the car list.
        """
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(choice(COLORS))
        car.goto(320, randint(-240, 240))
        self.cars.append(car)

    def move_cars(self):
        """
        Moves all cars in the car list to the left by the current car speed.
        """
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        """
        Increases the speed at which cars move.
        """
        self.car_speed += MOVE_INCREMENT

    def remove_offscreen_cars(self):
        """
        Removes cars that have moved off the left edge of the screen from the car list.
        """
        for car in self.cars[:]:
            if car.xcor() < -340:
                car.hideturtle()
                self.cars.remove(car)