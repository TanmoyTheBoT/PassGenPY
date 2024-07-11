from tkinter import *
import string
import random
import pyperclip
import os
import datetime

# Initialize a variable to store the last generated password
last_generated_password = ""

def generator():
    global last_generated_password

    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all_characters = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_Box.get())

    while True:
        strength = strength_var.get()
        if strength == "Weak":
            random_password = ''.join(random.choice(small_alphabets) for _ in range(password_length))
        elif strength == "Medium":
            random_password = ''.join(random.choice(small_alphabets + capital_alphabets) for _ in range(password_length))
        elif strength == "Strong":
            random_password = ''.join(random.choice(all_characters) for _ in range(password_length))

        if random_password != last_generated_password:
            break

    last_generated_password = random_password

    # Get user input for username/email and website name
    username_email = usernameEmailField.get()
    website_name = websiteNameField.get()

    # Display the generated password
    passwordField.delete(0, END)
    passwordField.insert(0, random_password)

    # Automatically copy the generated password to the clipboard
    pyperclip.copy(random_password)

    # Save all relevant information to the text file
    desktop_path = os.path.expanduser("~/Desktop")
    file_path = os.path.join(desktop_path, "generated_passwords.txt")

    with open(file_path, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - Website: {website_name} | Username/Email: {username_email} | Password: {random_password}\n")

root = Tk()
root.config(bg='gray20')
Font = ('serif', 13)
root.title("PassGenPy")  # Set the window title
root.resizable(False, False)  # Disable window resizing


# for background image

# Load the  (replace 'background.png' with your actual image file)
# bg_image = PhotoImage(file="D:\\Tanmoy\\VS\\python\\background.png")

# Create a Label widget to display the image
# background_label = Label(root, image=bg_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Stretch the image to cover the entire window

# for background image




passwordLabel = Label(root, text='PassGenPy', font=('times new roman', 20, 'bold'), bg='gray20', fg='white')
passwordLabel.grid(pady=10)

strength_var = StringVar()
strength_var.set("Medium")

strengthDropdown = OptionMenu(root, strength_var, "Weak", "Medium", "Strong")
strengthDropdown.grid(pady=5)

lengthLabel = Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
lengthLabel.grid(pady=5)

length_Box = Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.delete(0, END)
length_Box.insert(0, 11)
length_Box.grid(pady=5)

# Add input fields for username/email and website name
usernameEmailLabel = Label(root, text='Username/Email', font=Font, bg='gray20', fg='white')
usernameEmailLabel.grid(pady=5)

usernameEmailField = Entry(root, width=25, bd=2, font=Font)
usernameEmailField.grid()

websiteNameLabel = Label(root, text='Website Name', font=Font, bg='gray20', fg='white')
websiteNameLabel.grid(pady=5)

websiteNameField = Entry(root, width=25, bd=2, font=Font)
websiteNameField.grid()

generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)

passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid()

root.mainloop()
