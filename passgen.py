from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import os
import datetime

# Initialize a variable to store the last generated password
last_generated_password = ""
generated_passwords = set()

# Load previously generated passwords from log file
script_directory = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(script_directory, "generated_passwords_log.txt")

if os.path.exists(log_file_path):
    with open(log_file_path, "r") as file:
        for line in file:
            generated_passwords.add(line.strip())

def generator():
    global last_generated_password, generated_passwords

    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    try:
        password_length = int(length_Box.get())
        if password_length < 12 or password_length > 256:
            raise ValueError("Password length must be between 12 and 256")
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))
        return

    while True:
        strength = strength_var.get()
        if strength == "Weak":
            random_password = ''.join(random.choice(small_alphabets + capital_alphabets) for _ in range(password_length))
            if (any(char in small_alphabets for char in random_password) and
                any(char in capital_alphabets for char in random_password) and
                random_password not in generated_passwords):
                break
        elif strength == "Medium":
            random_password = ''.join(random.choice(small_alphabets + capital_alphabets + numbers) for _ in range(password_length))
            if (any(char in small_alphabets for char in random_password) and
                any(char in capital_alphabets for char in random_password) and
                any(char in numbers for char in random_password) and
                random_password not in generated_passwords):
                break
        elif strength == "Strong":
            random_password = ''.join(random.choice(small_alphabets + capital_alphabets + numbers + special_characters) for _ in range(password_length))
            if (any(char in small_alphabets for char in random_password) and
                any(char in capital_alphabets for char in random_password) and
                any(char in numbers for char in random_password) and
                any(char in special_characters for char in random_password) and
                random_password not in generated_passwords):
                break

    last_generated_password = random_password
    generated_passwords.add(random_password)

    with open(log_file_path, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Timestamp: {timestamp} | Strength: {strength} | Password: {random_password}\n")

    passwordField.delete(0, END)
    passwordField.insert(0, random_password)

def copy_to_clipboard():
    random_password = passwordField.get()
    username_email = usernameEmailField.get()
    website_name = websiteNameField.get()

    if not random_password:
        messagebox.showerror("No Password", "Please generate a password first.")
        return

    pyperclip.copy(random_password)

    file_path = os.path.join(script_directory, "generated_passwords.txt")

    with open(file_path, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Timestamp: {timestamp} | Website: {website_name} | Username/Email: {username_email} | Password: {random_password}\n")

    # Update the text on the copyButton to show "Copied"
    copyButton.config(text="Copied", state=DISABLED)

    # After a delay, revert the button back to its original state
    root.after(2000, lambda: copyButton.config(text="Copy", state=NORMAL))

# Function to clear all fields
def clear_fields():
    usernameEmailField.delete(0, END)
    websiteNameField.delete(0, END)
    passwordField.delete(0, END)
    length_Box.delete(0, END)
    length_Box.insert(0, 12)
    strength_var.set("Strong")

# Create the main window
root = Tk()
root.config(bg='gray20')
Font = ('Arial', 13)
root.title("PassGenPy")
root.resizable(False, False)

# Title label
passwordLabel = Label(root, text='PassGenPy', font=('Arial', 20, 'bold'), bg='gray20', fg='white')
passwordLabel.grid(pady=10, row=0, columnspan=2)

# Strength selection dropdown
strength_var = StringVar()
strength_var.set("Strong")
strengthDropdown = OptionMenu(root, strength_var, "Weak", "Medium", "Strong")
strengthDropdown.config(bg='gray30', fg='white', font=Font, width=10, relief=FLAT)
strengthDropdown.grid(pady=5, row=1, column=1, sticky=W)

strengthLabel = Label(root, text='Strength', font=Font, bg='gray20', fg='white')
strengthLabel.grid(pady=5, row=1, column=0, sticky=E)

# Password length label and spinbox
lengthLabel = Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
lengthLabel.grid(pady=5, row=2, column=0, sticky=E)
length_Box = Spinbox(root, from_=12, to_=256, width=5, font=Font)
length_Box.config(bg='gray30', fg='white', bd=2, relief=FLAT)
length_Box.delete(0, END)
length_Box.insert(0, 12)
length_Box.grid(pady=5, row=2, column=1, sticky=W)

# Username/Email input
usernameEmailLabel = Label(root, text='Username/Email', font=Font, bg='gray20', fg='white')
usernameEmailLabel.grid(pady=5, row=3, column=0, sticky=E)
usernameEmailField = Entry(root, width=25, bd=2, font=Font)
usernameEmailField.config(bg='gray30', fg='white')
usernameEmailField.grid(row=3, column=1, sticky=W)

# Website name input
websiteNameLabel = Label(root, text='Website Name', font=Font, bg='gray20', fg='white')
websiteNameLabel.grid(pady=5, row=4, column=0, sticky=E)
websiteNameField = Entry(root, width=25, bd=2, font=Font)
websiteNameField.config(bg='gray30', fg='white')
websiteNameField.grid(row=4, column=1, sticky=W)

# Generate button
generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.config(bg='gray30', fg='white', bd=2, relief=RAISED)
generateButton.grid(pady=5, row=5, columnspan=2)

# Password display field
passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.config(bg='gray30', fg='white')
passwordField.grid(row=6, columnspan=2)

# Copy button
copyButton = Button(root, text='Copy', font=Font, command=copy_to_clipboard)
copyButton.config(bg='gray30', fg='white', bd=2, relief=RAISED)
copyButton.grid(pady=5, row=7, columnspan=2)

# Clear button
clearButton = Button(root, text='Clear', font=Font, command=clear_fields)
clearButton.config(bg='gray30', fg='white', bd=2, relief=RAISED)
clearButton.grid(pady=5, row=8, columnspan=2)

# Start the main loop
root.mainloop()
