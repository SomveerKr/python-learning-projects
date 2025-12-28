from turtle import Turtle

class Paddle(Turtle):
    """A class to represent the paddle in a ping pong game."""
    
    def __init__(self, position):
        """Initializes the paddle at the given position and sets its shape, color, and size."""
        super().__init__() 
        self.shape("square") 
        self.color("white") 
        self.shapesize(stretch_wid=5, stretch_len=1) 
        self.penup()
        self.goto(position)
    # --- Paddle Movement Functions ---
    def move_up(self):
        """Moves the paddle up by a fixed step, unless it would go off the top of the screen."""
        y = self.ycor()
        # Prevent paddle from going too high (e.g., beyond the top of the screen)
        if y < 290 - 50:
            self.goto(self.xcor(), y + 80) 
    def move_down(self):
        """Moves the paddle down by a fixed step, unless it would go off the bottom of the screen."""
        y = self.ycor()
        # Prevent paddle from going too low (e.g., beyond the bottom of the screen)
        if y > -290 + 50: 
            self.goto(self.xcor(), y - 80) 
            
