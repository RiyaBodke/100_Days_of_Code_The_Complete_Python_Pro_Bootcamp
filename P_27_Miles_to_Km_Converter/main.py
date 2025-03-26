from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

mile_input = Entry(width=8)
mile_input.grid(row=0, column=1)

mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)

text_label = Label(text="is equal to")
text_label.grid(row=1, column=0)

answer_label = Label(text=0)
answer_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

def Calculate():
    """ This function is used to calculate km from miles"""
    
    miles = float(mile_input.get())
    answer = round(1.609 * miles)
    answer_label.config(text=answer)

button = Button(text="Calculate", command=Calculate)
button.grid(row=2, column=1)

window.mainloop()
