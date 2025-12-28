STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


from turtle import Turtle

class Player(Turtle):
    """
    Represents the player-controlled turtle. Handles movement and position reset.
    Inherits from Turtle for drawing and movement.
    """
    def __init__(self):
        """
        Initializes the player turtle, sets its shape, starting position, and heading.
        """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        """
        Moves the player turtle up by a fixed distance.
        """
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def move_down(self):
        """
        Moves the player turtle down by a fixed distance.
        """
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def has_reached_finish_line(self):
        """
        Checks if the player has reached the finish line at the top of the screen.
        Returns:
            bool: True if at or above the finish line, False otherwise.
        """
        return self.ycor() >= FINISH_LINE_Y
    
    def reset_position(self):
        """
        Resets the player turtle to the starting position at the bottom of the screen.
        """
        self.goto(STARTING_POSITION)