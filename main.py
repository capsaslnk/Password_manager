import csv
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def password_generator():

    password_input.delete(0, END)
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    random_password = "".join(password_list)
    password_input.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_record():

    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {website: {"email": username, "password": password}}

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Fields are empty", message="Please don't leave fields empty"
        )

    else:
        try:
            with open("data.json", "r") as file:
                # Loading the old Data from JSON
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating the Data in JSON
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving the updated data
                json.dump(data, file, indent=4)

        website_input.delete(0, END)
        username_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #


def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            # Loading the old Data from JSON
            data = json.load(file)
            search_data = data[website]
    except KeyError:
        messagebox.showinfo(
            title="Site Details not Found", message="There is no data available for this site"
        )
    except FileNotFoundError:
        messagebox.showinfo(
            title="File not Found", message="No data file is available"
        )
    else:
        messagebox.showinfo(
            title={website}, message=f"Email: {search_data["email"]}\nPassword: {search_data["password"]}"
        )


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

# Inputs
website_input = Entry(width=25)
website_input.grid(row=1, column=1, sticky=E)
website_input.focus()

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=25)
password_input.grid(row=3, column=1, sticky=E)

# Buttons
generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(row=3, column=2, sticky=W + E)

add_button = Button(text="Add", width=36, command=add_record)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky=W + E)

window.mainloop()
