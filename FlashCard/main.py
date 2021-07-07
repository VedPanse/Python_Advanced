import random
from tkinter import *
import pandas
data = pandas.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient="records")
print(to_learn)
BACKGROUND_COLOR = "#B1DDC6"


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

unknown = PhotoImage(file="images/wrong.png")
check = PhotoImage(file="images/right.png")

wrong_button = Button(image=unknown, highlightthickness=0, width=50, height=50, command=next_card)
wrong_button.grid(column=0, row=1)

correct_button = Button(image=check, highlightthickness=0, width=50, height=50, command=next_card)
correct_button.grid(column=1, row=1)

next_card()
window.mainloop()
