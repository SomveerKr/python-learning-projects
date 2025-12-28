FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    """
    Manages the game scoreboard, displaying the current level and handling game over messages.
    Inherits from Turtle for drawing on the screen.
    """
    def __init__(self):
        """
        Initializes the scoreboard, sets the starting level, and positions the scoreboard on the screen.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.level = 1
        self.update_level
    def update_level(self):
        """
        Clears the previous level display and writes the current level at the top left of the screen.
        """
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)
    def game_over(self):
        """
        Displays the 'GAME OVER' message at the center of the screen.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def increase_level(self):
        """
        Increases the level by 1 and updates the scoreboard display.
        """
        self.level+=1
        self.update_level()