# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy
from json import dump, load, JSONDecodeError

# ---------------------------- CONSTANTS ------------------------------- #
GREY = "#302f2f"
IMG_PATH = "./logo.png"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    
    if len(password_input.get()) !=0:
        password_input.delete(0, END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)
        
    generated_password = "".join(password_list)
    password_input.insert(0, str(generated_password))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """Function to collect password details"""
    
    # Saving User Inputs
    website = website_input.get()
    user_name = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "user name" : user_name,
            "password" : password,
        }
    }
    
    copy(password)
    
    if (len(website)==0) or (len(password)==0):
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
    #     is_ok = messagebox.askokcancel(title=website_name, message=f"You have entered these details:\nUser Name : {user_name}\nPassword : {password}\n\nShould we save this?")
    
    # if is_ok:
        
        # Writing Details in File
        
        try:
            # Open file in Read format
            with open("./data.json", "r") as file:
                data = load(file)           # Read file 
                data.update(new_data)   # Update old data with new data

        except (FileNotFoundError, JSONDecodeError):
            data = new_data
            data.update(new_data)

        finally:
        # Open file in Write format
            with open("./data.json", "w") as file:
                dump(data, file, indent=4)  # Write or Save updated data
            
            # Clearing User Input
            website_input.delete(0, END)
            username_input.delete(0 ,END)
            username_input.insert(0 ,"xxx@gmail.com")
            password_input.delete(0, END)
            
            messagebox.showinfo(title ="Done", message="Details saved !\n\nPassword is copied to clipboard.\nUse it to create your account.")

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    print("Button Pressed")
    
    website_name = website_input.get()
    
    try:
        with open("data.json", "r") as file:
            data = load(file)
    except (FileNotFoundError, JSONDecodeError):
        messagebox.showerror(title="Error", message="You have no passwords saved !")
    else:
        if website_name in data:
            saved_user_name = data[website_name]["user name"]
            saved_password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"User Name : {saved_user_name}\nPassword : {saved_password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website_name} exits.")

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="black")

# Logo
logo_canvas = Canvas(width=200, height=200, highlightthickness=0, bg="black")
logo = PhotoImage(file=IMG_PATH)
logo_canvas.create_image(100, 100, image=logo)
logo_canvas.grid(row=0, column=1)

# Website Text
website_text = Label(text="Website :", bg="black")
website_text.grid(row=1, column=0)

# Website Input
website_input = Entry(width=21, highlightthickness=0, highlightbackground="black", border=0, bg=GREY)
website_input.grid(row=1, column=1)
website_input.focus()

# Search Button
search_button = Button(text = "Search", command = search_password, width=13, highlightthickness=0, highlightbackground="black")
search_button.grid(row=1, column=2)

# Username Text
username_text = Label(text="Email/Username :", bg="black")
username_text.grid(row=2, column=0)

# Username Input
username_input = Entry(width=38, highlightthickness=0, highlightbackground="black", border=0, bg=GREY, )
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "xxx@gmail.com")

# Password Text
password_text = Label(text="Password :", bg="black")
password_text.grid(row=3, column=0)

# Password Input
password_input = Entry(width=21, highlightthickness=0, highlightbackground="black", border=0, bg=GREY)
password_input.grid(row=3, column=1)

# Generate Password Button
generate_button = Button(text="Generate Password", command=generate_password, highlightthickness=0, highlightbackground="black")
generate_button.grid(row=3, column=2)

# Add Button
add_button = Button(text="Add",command=save_password, width=36, highlightthickness=0, highlightbackground="black")
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
