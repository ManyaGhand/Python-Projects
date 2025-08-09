from tkinter import *
from tkinter import PhotoImage
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Germanwords.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn= data.to_dict(orient ="records")

# ------------------------- NEW CARD ----------------------------- #

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(image, image=card_front_image)
    canvas.itemconfig(word_text ,text = current_card["German"], fill = "black")
    canvas.itemconfig(title_text, text="German", fill = "black")
    window.after(3000, func=flip_card)

# ------------------------- FLIP CARD ---------------------------- #

def flip_card():
    canvas.itemconfig(image , image = card_back_image)
    canvas.itemconfig(title_text , text = "English", fill = "white")
    canvas.itemconfig(word_text, text = current_card["English"], fill = "white")


# ------------------------ REMOVE CARD --------------------------- #

def remove_cards():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index = False)
    next_card()

# ------------------------- UI SETUP ----------------------------- #

window = Tk()
window.title("Flashcards")
window.config(padx = 50 , pady = 50, bg = BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#CANVAS
canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness = 0)
card_front_image = PhotoImage(file = "images/card_front.png")
card_back_image = PhotoImage(file = "images/card_back.png")
image = canvas.create_image(400, 263 , image = card_front_image)
canvas.grid(row = 0 , column = 0 , columnspan = 2)

#CANVAS TEXT
title_text = canvas.create_text(400 , 150 , text = "", font = ("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263 , text = "", font = ("Ariel", 60, "bold"))

#BUTTONS
right_sign: PhotoImage = PhotoImage(file = "images/right.png")
right_button = Button(image = right_sign, highlightthickness= 0, command = remove_cards)
right_button.grid(row = 1, column = 0)

wrong_sign = PhotoImage(file = "images/wrong.png")
wrong_button = Button(image = wrong_sign, highlightthickness= 0, command = next_card)
wrong_button.grid(row = 1, column = 1)

next_card()

window.mainloop()
