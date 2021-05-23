from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Saves inputted data in .txt
def save():
    # Gets data from entries
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # User checks if entered data is ok. If is - saves data in .txt
    if not website or not username or not password:
        messagebox.askokcancel(title="NO DATA", message="INPUT DATA OR CHARON WILL TAKE YOU TO HADES")
    else:
        # Pop-up for user
        is_ok = messagebox.askokcancel(title=website, message=f"These are the detailes entered: \nEmail: {username}"
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("PASSWORDS.txt", "a") as PASSWORDS:
                PASSWORDS.write(f"\nWEBSITE: {website}"
                                f"\nUSERNAME: {username}"
                                f"\nPASSWORD: {password}"
                                f"\n------------------------------------------------")
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Sets up a main window of program
window = Tk()
window.title("Cerberus")
window.config(padx=20, pady=20)

# Loads and sets up an image
canvas = Canvas(width=400, height=300, highlightthickness=0)
cerber_img = PhotoImage(file="cerber.png")
canvas.create_image(200, 150, image=cerber_img)
canvas.grid(column=1, row=0, columnspan=3)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=43)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=43)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=41, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
