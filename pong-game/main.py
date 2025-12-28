"""
Main game loop for the Ping Pong Game.

Sets up the screen, paddles, ball, and scoreboard, and runs the main game loop handling user input, ball movement, collision detection, and scoring.
"""
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# --- Main Game Setup ---
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black") 
screen.title("Ping Pong Game")

screen.tracer(0)
# --- Paddle Setup ---
right_paddle = Paddle((380, 0)) 
left_paddle = Paddle((-380, 0))

# --- Ball Setup ---
ball = Ball()  # Create a ball instance

# --- Score Setup ---
scoreboard = Scoreboard()  # Create a score instance

# --- Keyboard Bindings ---
screen.listen() 
screen.onkey(right_paddle.move_up, "Up") 
screen.onkey(right_paddle.move_down, "Down") #
screen.onkey(left_paddle.move_up, "w")  # Move left paddle up with 'w'
screen.onkey(left_paddle.move_down, "s")  # Move left paddle down with

is_game_on = True  # Flag to control the game loop
while is_game_on:
    
    screen.update()  # Update the screen
    # Here you can add more game logic, such as ball movement, collision detection, etc.
    time.sleep(ball.move_speed)  # Control the speed of the game loop
    ball.move()
    # check for collision with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Bounce the ball off the top or bottom wall


    # check for collision with the paddles
    if (ball.xcor() > 340 and ball.distance(right_paddle) < 50) or (ball.xcor() < -340 and ball.distance(left_paddle) < 50):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        # print("Left player scores!")
        scoreboard.left_player_scores()
    if ball.xcor() < -380:
        ball.reset_position()
        # print("Right player scores!")
        scoreboard.right_player_scores()

screen.exitonclick()  # Wait for a click to exit the game