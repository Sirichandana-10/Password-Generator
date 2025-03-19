import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    try:
        # Get the length from user input
        length = int(length_entry.get())

        # Check if the length is valid
        if length <= 0:
            raise ValueError("Password length must be greater than zero.")

        # Define the characters to use in the password
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the generated password in the entry field
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to copy the generated password to clipboard
def copy_to_clipboard():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
tk.Label(root, text="Enter password length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
