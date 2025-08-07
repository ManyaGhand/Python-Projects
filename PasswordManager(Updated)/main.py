from tkinter import *
from tkinter import messagebox
from random import randint , shuffle , choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0 , password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
            website:{ "email" : email,
                      "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0 :
        messagebox.showinfo(title = "Oops", message = "Please don't leave any fields empty! ")

    else:
        try:
            with open("password.json", "r") as file:
                data = json.load(file) #Read the file
        except FileNotFoundError:
            with open("password.json", "w") as file:
                json.dump(new_data, file , indent = 4) #Create a file
        else:
            data.update(new_data)
            with open("password.json", "w") as file:
                json.dump(data, file , indent = 4) #Write into the existing file
        finally:
            website_input.delete(0 , END)
            password_input.delete(0 , END)

# ---------------------------- FIND PASSWORD -------------------------- #

def find_password():
    user_entry = website_input.get()
    try:
        with open("password.json", "r") as file:
            data = json.load(file)  # Read the file
    except FileNotFoundError:
        messagebox.showinfo(title="No File", message="No Data file Found ")
    else:
        if user_entry in data:
            email = data[user_entry]["email"]
            password = data[user_entry]["password"]
            messagebox.showinfo(title = user_entry , message = f" Email: {email}\n Password: {password} ")
        else:
            messagebox.showinfo(title="Error", message=f"Your website {user_entry} doesn't exist.")

# ---------------------------- UI SETUP ------------------------------- #

FONT = ("Calibre", 10)

window = Tk()
window.title("Password Manager")
window.config(padx = 50 , pady = 50)

#CANVAS
canvas = Canvas(width = 200, height = 200 , highlightthickness= 0 )
image = PhotoImage(file = "logo.png" )
canvas.create_image(100 , 100, image = image)
canvas.grid(row = 0 , column = 1)

#LABELS
website_label = Label(text = "Website:", font = FONT)
website_label.grid(row = 1, column = 0)

email_label = Label(text ="Email/Username:", font = FONT)
email_label.grid(row = 2, column = 0)

Password_label = Label(text = "Password:", font = FONT)
Password_label.grid(row = 3, column = 0)

#ENTRIES
website_input = Entry(width = 30)
website_input.grid(row = 1 , column = 1 )
website_input.focus()

email_input = Entry(width = 49)
email_input.grid(row = 2, column = 1, columnspan = 2)
email_input.insert(0, "manya@gmail.com")

password_input = Entry(width = 30)
password_input.grid(row = 3, column = 1, padx = (0,2))

#BUTTONS
generate_password_button = Button(text = "Generate Password", width = 14, command = generate_password, highlightthickness= 0)
generate_password_button.grid(row = 3, column = 2 , padx = (0, 5))

add_button = Button(text = "Add", width = 42, command = save_password)
add_button.grid(row = 4, column = 1, columnspan = 2, pady = 2)

search_button = Button(text = " Search ", width = 13,highlightthickness= 0, command = find_password)
search_button.grid(row = 1 , column = 2 , columnspan = 2,  padx = (0, 5))

window.mainloop()
