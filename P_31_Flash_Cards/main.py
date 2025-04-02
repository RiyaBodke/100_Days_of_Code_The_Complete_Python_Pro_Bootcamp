import pandas as pd
from random import randint
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pd.read_csv("./data/revised_data.csv")
    
except FileNotFoundError:
    df = pd.read_csv("./data/english_words.csv")
    words = df.to_dict()
    
else:
    words = df.to_dict()

n=0
word = ""
meaning = ""

def new_card():
    
    """This function is used to display a new flash card"""
    
    global n,word
    n = randint(0, 506)
    word = words["Word"][n]
    
    card_canvas.itemconfig(card_image,image=FRONT_CARD_IMG)
    card_canvas.itemconfig(title_text, text= "Word")
    card_canvas.itemconfig(word_text, text=word)
    # print(f"{meaning}")
    
    window.after(5000, turn_flashcard)

def turn_flashcard():
    
    """This function is used to turn the flash card and display the meaning of the word"""
    
    global n, meaning
    meaning = words["Meaning"][n]
    
    card_canvas.itemconfig(card_image, image=BACK_CARD_IMG)
    card_canvas.itemconfig(title_text, text= "Meaning")
    card_canvas.itemconfig(word_text, text=meaning)
    
def known_word():
    
    """This function is used to remove knonwn words from the flash cards"""
    
    global n
    del words["Word"][n]
    del words["Meaning"][n]
    
    new_df = pd.DataFrame(words)
    new_df.to_csv("./data/revised_data.csv", index=False)
    
    new_card()

# Window
window = Tk()
window.title("Vocab Exam-Prep")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create Card Background Images 
FRONT_CARD_IMG = PhotoImage(file="./images/card_front.png")
BACK_CARD_IMG = PhotoImage(file="./images/card_back.png")

# Front Card Canvas
card_canvas = Canvas(width=800, height = 526, highlightthickness=0, bg=BACKGROUND_COLOR)

# Card Image
card_image = card_canvas.create_image(400, 263, image="")

# Title Text
title_text = card_canvas.create_text(400, 150, text="", font = ("Ariel", 35, "italic"), fill="black")

# Word Text
word_text = card_canvas.create_text(400, 263, text="", font=("Ariel", 50, "bold"), fill="black", width=800)
card_canvas.grid(row=0,column=0, columnspan=2)

new_card()

# Wrong Button
cross_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_img, command=new_card, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

# Right Button
tick_img = PhotoImage(file="./images/right.png")
right_canvas = Button(image=tick_img, command=known_word, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
right_canvas.grid(row=1, column=1)

window.mainloop()