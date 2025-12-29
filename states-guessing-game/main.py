
import pandas as pd
import turtle


# using pandas to read the csv file
states_and_uts = pd.read_csv("states_uts.csv")


#using turtle to create a map of India
screen = turtle.Screen()
screen.title("Guess the State of India")
screen.setup(width=760, height=860)
screen.bgpic("India.gif")
# Create a turtle to write the state names
t = turtle.Turtle()
t.penup()
t.hideturtle()  
t.speed(0)

#Get the state name input from the user
def get_state_name(score, total_states):
    state_name = screen.textinput(title=f"{score}/{total_states} Guess are Correct.", prompt="Enter the name of the state or union territory:").title()
    return state_name

# Function to write the state name on the map
def write_state_name(state_name, x, y):
    t.goto(x, y)
    t.color("black")
    t.write(state_name, align="center", font=("Arial", 11, "normal"))

# Initializing the game
# List of all states and union territories
all_states = states_and_uts["state"].tolist()
score = 0
guessed_states = []


while score < len(all_states):
    state_name = get_state_name(score, len(all_states))
    if state_name == "Exit":
        print("Exiting the game.")
        break
    # Check if the state name is in the list (case-insensitive, title case)
    matched_row = states_and_uts[states_and_uts["state"] == state_name]
    if not matched_row.empty:
        # State is present
        print("State found!")
        x = int(matched_row.iloc[0]["x"])
        y = int(matched_row.iloc[0]["y"])
        write_state_name(state_name, x, y)
        score += 1
        guessed_states.append(state_name)
    else:
        print("State not found.")


# Show praise if all states guessed correctly
if score == len(all_states):
    t.goto(0, 0)
    t.color("green")
    t.write("Congratulations! You guessed all 36 states correctly!", align="center", font=("Arial", 18, "bold"))

# After the game ends

missed_states = [state for state in all_states if state not in guessed_states]
if missed_states:
    pd.to_csv("missed_states.csv", index=False)



