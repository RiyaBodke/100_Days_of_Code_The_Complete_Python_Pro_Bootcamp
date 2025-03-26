# ---------------------------- IMPORTS ------------------------------- #

from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
PATH = "./tomato.png"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    
    print("Reset button is pressed!")
    start_button.config(state="normal")
    reset_button.config(state="disabled")
    
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def bring_to_front():
    # Restore if window is minimized
    window.state("normal")
    # Bring to top level above all windows
    window.attributes("-topmost", True)
    # Allows other windows to top level again
    window.attributes("-topmost", False)

def count_down(count):
    
    count_min = floor(count/60)
    count_sec = count%60
    
    if count_min == 0 and count_sec < 3:
        bring_to_front()
        window.bell()
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
    
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else :
        start_timer()
        mark = ""
        work_sessions = floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        tick_label.config(text=mark)
        
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    
    global reps
    reps += 1
    
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    
    if (reps % 8) == 0 :
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif (reps % 2) == 0 :
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    
    print("Start button is pressed!")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 55, "bold"))
title_label.grid(row=0, column=1)

img = PhotoImage(file=PATH)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100,112, image = img)
timer_text = canvas.create_text(100, 130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(width=10,text="Start", highlightbackground=YELLOW, command=start_timer, state="normal")
start_button.grid(row=2, column=0)

tick_label = Label(bg=YELLOW, fg=GREEN)
tick_label.grid(row=3, column=1)

reset_button = Button(width=10, text="Reset",command = reset ,highlightbackground=YELLOW, bg=GREEN, state="disabled")
reset_button.grid(row=2, column=2)


window.mainloop()