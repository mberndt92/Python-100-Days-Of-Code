from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"


def wrong_btn_clicked():
    global data
    if len(data) == 0:
        data = pandas.read_csv("./data/french_words.csv").to_dict(orient="records")
    next_word()


def right_btn_clicked():
    global data, current_card
    data.remove(current_card)
    next_word()


def show_result():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)


def game_over():
    global flip_timer
    screen.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text="You learned everything :)", fill="black")
    canvas.itemconfig(card_word, text="Press X button to start over", fill="black")


def next_word():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    save_progress()
    if len(data) == 0:
        game_over()
    else:
        current_card = random.choice(data)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas.itemconfig(canvas_image, image=card_front_image)
        flip_timer = screen.after(3000, show_result)


def save_progress():
    global data
    dataframe = pandas.DataFrame(data=data)
    dataframe.to_csv("./data/words_to_learn.csv", index=False)


# Global current_card
current_card = {}

# Load the CSV
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    data.to_csv("./data/words_to_learn.csv")

data = data.to_dict(orient="records")

# Create the User Interface
screen = Tk()
screen.title("Flashy")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Front/Back
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
# Uses X & Y position as CENTER -> thus need to put width/2 & height/2
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text=f"Word", font=("Ariel", 60, "bold"))

# Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=wrong_btn_clicked)
right_btn = Button(image=right_image, highlightthickness=0, borderwidth=0, command=right_btn_clicked)

# Grid Placement
canvas.grid(row=0, column=0, columnspan=2)
wrong_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=1)

flip_timer = screen.after(3000, show_result)
next_word()

screen.mainloop()
