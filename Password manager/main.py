import tkinter
import random
import pyperclip
import json
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "Email/Username" : email,
            "Password" : password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Tile",message="Please don't leave any fields empty!")
        return
    else:
        try:
            with open("json_file", "r") as data_file:
                #reads old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("json_file", "w") as data_file:
                #saving new data
                json.dump(new_data, data_file, indent=4)
        else:
            #update old data with new data
            data.update(new_data)
            with open("json_file", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open("json_file", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message= "Data file doesn't exist")
    else:
        if website in data:
            email = data[website]["Email/Username"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email/Username: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details of the website exists.")

# ---------------------------- UI SETUP ------------------------------- #

#window
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

#canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

#website Label:
website_label = Label(text="Website:", anchor="w")
website_label.grid(column=0, row=1, sticky="W")

#website Entry:
website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")
website_entry.focus()

#Email/username Label:
email_label = Label(text="Email/Username:", anchor="w")
email_label.grid(column=0, row=2, sticky="W")

#email Entry
email_entry = Entry(width=57)
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")
email_entry.insert(0,"example@email.com")

#password Label:
password_label = Label(text="Password:", anchor="w")
password_label.grid(column=0, row=3, sticky="W")

#password Entry:
password_entry = Entry(width=38)
password_entry.grid(column=1, row=3, sticky="W")

#Generate password button:
generate_password = Button(text="Generate Password", width=14, command=generate_password)
generate_password.grid(column=2, row=3)

#Add button:
add_button = Button(text="Add", width=48, command= save)
add_button.grid(column=1, row=4, columnspan=2)

#Search Button
search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(column=2, row=1)
window.mainloop()