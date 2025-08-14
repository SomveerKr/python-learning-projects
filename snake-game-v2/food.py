from turtle import Turtle
import random
class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("brown")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Make the food smaller
        self.speed("fastest")
        self.refresh()  # Place the food at a random position when initialized
        
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)