from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please make sure you haven't left any of the fields empty")
    else:
        save_to_file(website=website, email=email, password=password)
        clear_inputs()


def search():
    search_key = website_entry.get()
    result = ""
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            search_result = data[search_key]
    except FileNotFoundError:
        pass
    except KeyError as error_message:
        print(f"There was a key error for key: {error_message}")
        messagebox.showerror(title="404", message=f"Couldn't find a password entry for: {error_message}")
    else:
        message = f"Website: {search_key}\nEmail/Username: {search_result["email"]}\nPassword: {search_result["password"]}"
        messagebox.showinfo(title="Password", message=message)


def save_to_file(website, email, password):
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        # Create file
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", mode="w") as file:
            json.dump(data, file, indent=4)

    messagebox.showinfo(title="Success", message="Password successfully saved.")


def clear_inputs():
    website_entry.delete(0, END)
    # email_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.config(width=200, height=200, padx=20, pady=50)
screen.title("Password Manager")

# Logo
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image, anchor=CENTER)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=18)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_btn = Button(text="Search", width=13, command=search)
search_btn.grid(column=2, row=1)

# Email / Username
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.insert(END, "maximilian_berndt@icloud.com")
email_entry.grid(column=1, row=2, columnspan=2)

# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)

# Add Button
add_btn = Button(text="Add", width=33, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

screen.mainloop()