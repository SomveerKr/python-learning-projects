from turtle import Screen, Turtle
import time
STARTING_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]  # Initial positions of the snake segments
MOVE_DISTANCE = 20  # Distance the snake moves each time
UP = 90  # Angle for moving up
DOWN = 270  # Angle for moving down
LEFT = 180  # Angle for moving left
RIGHT = 0  # Angle for moving right
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # The first segment is the head of the snake

    def create_snake(self):
        for postion in STARTING_POSITIONS:
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.goto(postion)
            self.segments.append(square)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Move the head of the snake forward
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def write(self, text, align="center"):
        self.head.write(text, align=align, font=("Arial", 16, "normal"))
        # Clear the text after a short delay
        time.sleep(1)
        self.head.clear()