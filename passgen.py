from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all_characters = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_Box.get())

    random_password = ""  # Initialize the variable outside the if statements

    strength = strength_var.get()
    if strength == "Weak":
        random_password = ''.join(random.choice(small_alphabets) for _ in range(password_length))
    elif strength == "Medium":
        random_password = ''.join(random.choice(small_alphabets + capital_alphabets) for _ in range(password_length))
    elif strength == "Strong":
        random_password = ''.join(random.choice(all_characters) for _ in range(password_length))

    passwordField.delete(0, END)  # Clear any existing content
    passwordField.insert(0, random_password)

    # Automatically copy the generated password to the clipboard
    pyperclip.copy(random_password)

root = Tk()
root.config(bg='gray20')
Font = ('serif', 13)

passwordLabel = Label(root, text='PassGenPy', font=('times new roman', 20, 'bold'), bg='gray20', fg='white')
passwordLabel.grid(pady=10)

strength_var = StringVar()
strength_var.set("Medium")  # Default strength selection

strengthDropdown = OptionMenu(root, strength_var, "Weak", "Medium", "Strong")
strengthDropdown.grid(pady=5)

lengthLabel = Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
lengthLabel.grid(pady=5)

length_Box = Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.delete(0, END)  # Clear any existing content
length_Box.insert(0, 11)  # Set default password length to 11
length_Box.grid(pady=5)

generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)

passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid()

root.mainloop()
