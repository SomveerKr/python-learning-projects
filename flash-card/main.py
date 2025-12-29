from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import randint, choice

BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None
current_card = {}
try:
    df= pd.read_csv("data/words_to_learn.csv")
    
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
    words_to_learn =  df.to_dict(orient="records")
    print(words_to_learn)
else:
    words_to_learn =  df.to_dict(orient="records")
#---- generate next word of the card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_img_item, image=card_back_img)


def generate_next_card():
    global flip_timer, current_card
    if flip_timer:
        window.after_cancel(flip_timer)
    current_card = choice(words_to_learn)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text= f"{current_card["French"]}", fill="black")
    canvas.itemconfig(card_img_item, image=card_front_img)
        
    flip_timer = window.after(3000, flip_card)
def user_knows_word():
    # Handle logic for "known" button
    print("User clicked: Known")
    generate_next_card()
    words_to_learn.remove(current_card)
    new_df = pd.DataFrame(words_to_learn)
    new_df.to_csv('data/words_to_learn.csv', index=False)





window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img_item = canvas.create_image(400, 263, image=card_front_img)



card_title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

#----------Buttons
right_mark_img = PhotoImage(file="images/right.png")
cross_mark_img = PhotoImage(file="images/wrong.png")

known_btn = Button(image=right_mark_img, command=user_knows_word)
known_btn.grid(row=1, column=0)

unknown_btn = Button(image=cross_mark_img, command=generate_next_card)
unknown_btn.grid(row=1, column=1)


generate_next_card()

window.mainloop()