from turtle import Screen, Turtle
import time
from snake import Snake 
from food import Food 
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off the screen updates for better performance


# Create an instance of the Snake class
snake = Snake()
food = Food()  # Create an instance of the Food class
scoreboard = Scoreboard()  # Create an instance of the Scoreboard class
screen.listen()  # Start listening for key presses
# Bind the arrow keys to the snake's movement methods
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def play_game():
    game_is_on = True
    while game_is_on:
        screen.update()  # Manually update the screen
        time.sleep(0.15)
        snake.move()  # Move the snake
        # Check for collision with food
        if snake.head.distance(food) < 15:
            print("Food eaten!")
            food.refresh()
            # extend the snake and increase the score
            snake.extend()
            scoreboard.increase_score()
            
            
        # Check for collision with the wall
        if(snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290):
            print("Game Over")
            # game_is_on = False
            scoreboard.reset()
            snake.reset()

        #Detect collision with the tail
        for segment in snake.segments[1:]:  # Skip the head
            if snake.head.distance(segment) < 10:
                print("Game Over")
                # game_is_on = False
                scoreboard.reset()
                snake.reset()

play_game()


screen.exitonclick()