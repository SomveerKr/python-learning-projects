from turtle import Turtle

class Ball(Turtle):
    """
    Represents the game ball.
    """
    def __init__(self):
        """Initializes the ball at the center of the screen with default speed and direction."""
        super().__init__()
        self.shape("circle") 
        self.color("red")
        self.penup() 
        self.goto(0, 0)
        self.dx = 10           # Initial horizontal speed (change in x)
        self.dy = 10           # Initial vertical speed (change in y)
        self.move_speed = 0.1  # Speed of the ball movement, can be adjusted for difficulty

    def move(self):
        """Moves the ball by updating its position based on its current speed and direction."""
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)
        

    def bounce_x(self):
        """Reverses the ball's horizontal direction and slightly increases its speed."""
        self.dx *= -1
        self.move_speed *= 0.9 # Increase speed slightly on bounce

    def bounce_y(self):
        """Reverses the ball's vertical direction."""
        self.dy *= -1

    def reset_position(self):
        """Resets the ball to the center, reverses its vertical direction, and resets its speed."""
        self.goto(0, 0)
        self.bounce_y() # Reverse vertical direction for a new serve
        self.move_speed = 0.1  # Reset speed after scoring
