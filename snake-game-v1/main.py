from turtle import Screen, Turtle
import time
from snake import Snake 
screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off the screen updates for better performance


# Create an instance of the Snake class
snake = Snake()

screen.listen()  # Start listening for key presses
# Bind the arrow keys to the snake's movement methods
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()  # Manually update the screen
    time.sleep(0.2)
    snake.move()  # Move the snake




screen.exitonclick()