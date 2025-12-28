from turtle import Turtle

class Scoreboard(Turtle):
    """A class to represent the score in a ping pong game."""
    
    def __init__(self):
        """Initializes the scoreboard, sets up the display, and prepares the initial scores for both players."""
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        """Clears and updates the score display with the current scores for both players."""
        self.clear()
        self.write(f"Left: {self.score_left} Right: {self.score_right}", align="center", font=("Courier", 24, "normal"))

    def left_player_scores(self):
        """Increments the left player's score by 1 and updates the display."""
        self.score_left += 1
        self.update_score()

    def right_player_scores(self):
        """Increments the right player's score by 1 and updates the display."""
        self.score_right += 1
        self.update_score()