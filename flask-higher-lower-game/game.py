from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <h1>Guess a number between 0 and 10</h1>
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="gif">
    
    """


random_number=random.randint(0,10)
print(random_number)

too_low_message="Too low, try again!"
too_high_message="Too high, try again!"
correct_message="You found me"

def generate_message(message_text, message_color, message_image):
    return f"""
    <h1 style= "color: {message_color};">{message_text}</h1>
    <img src={message_image} >
    """

@app.route("/<int:guess_number>")
def guess_number(guess_number):
    if (guess_number == random_number):
        return generate_message(correct_message, "green","https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif")

    elif guess_number < random_number:
        return generate_message(too_low_message, "red","https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif")

    else:
        return generate_message(too_high_message, "purple","https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif")



if __name__ == "__main__":
    app.run(debug=True)