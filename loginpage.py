
import tkinter as tk
from tkinter import RIDGE, TOP, Frame, Label, messagebox

# Creating the main window
root = tk.Tk()
root.title("BoozeCAFE lOGIN FORM")
root.geometry("400x400")

# Function to authenticate the user
def authenticate_user():
    # Getting the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()
    
    # Check if the username and password are correct
    if username == "admin" and password == "admin123":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

# Creating the labels and text entry fields
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

# Creating the login button
login_button = tk.Button(root, text="Login", command=authenticate_user)
login_button.grid(row=2, column=1)



# Running the main loop
root.mainloop()
