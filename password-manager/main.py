from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters)) # OR the list comprehension below
    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols) # OR the list comprehension below
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers) # OR the list comprehension below
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_letters

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char # OR the code below to join the list elements
    password = "".join(password_list)

    password_entry.insert(0, password)  # writing it to the field
    pyperclip.copy(password)  # Copy the password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Fields cannot be empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reads current json data
                data = json.load(data_file)
        except FileNotFoundError:
            # Means there is no json file, yet.
            with open("data.json", "w") as data_file2:
                json.dump(new_data, data_file2, indent=4)
        else:
            # Updates data, by appending new_data to previous json object
            data.update(new_data)
            with open("data.json", "w") as data_file3:
                # Write into json file
                json.dump(data, data_file3, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    # if !is_ok then do nothing

# ---- Search entry ----- #


def find_password():
    website = website_entry.get()  # website entered on the form

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        #  File not found
        messagebox.showerror(title="Error", message="File not found!")
    else:
        #  file has been found
        if website in data:
            # website found in the file
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists!")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")  # extract from file system
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

website_entry = Entry(width=18)
website_entry.grid(column=1, row=1)
website_entry.focus()  # sets the cursor as initial position

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "prateek@gmail.com")  # prefill text, starting from position 0

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
