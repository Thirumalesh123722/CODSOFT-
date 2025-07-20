import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 6:
            messagebox.showwarning("Warning", "Password length should be at least 6!")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    characters = ""
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    output_entry.delete(0, tk.END)
    output_entry.insert(0, password)

# GUI Window
window = tk.Tk()
window.title(" Smart Password Generator")
window.geometry("400x350")
window.config(bg="#f2f2f2")

# Title Label
tk.Label(window, text="Password Generator", font=("Arial", 16, "bold"), bg="#f2f2f2").pack(pady=10)

# Length Input
tk.Label(window, text="Password Length:", bg="#f2f2f2").pack()
length_entry = tk.Entry(window)
length_entry.pack(pady=5)

# Character Options
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(window, text="Include UPPERCASE", variable=var_upper, bg="#f2f2f2").pack()
tk.Checkbutton(window, text="Include lowercase", variable=var_lower, bg="#f2f2f2").pack()
tk.Checkbutton(window, text="Include Numbers", variable=var_digits, bg="#f2f2f2").pack()
tk.Checkbutton(window, text="Include Symbols", variable=var_symbols, bg="#f2f2f2").pack()

# Generate Button
tk.Button(window, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

# Output
output_entry = tk.Entry(window, width=30, font=("Arial", 12))
output_entry.pack(pady=5)

# Run the app
window.mainloop()