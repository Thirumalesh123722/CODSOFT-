import tkinter as tk
from tkinter import messagebox

contacts = {}

# Core functions
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        messagebox.showinfo("Success", f"Contact '{name}' added.")
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Name and Phone are required!")

def view_contacts():
    display_text.delete("1.0", tk.END)
    if contacts:
        for name, details in contacts.items():
            display_text.insert(tk.END, f"\n{name}\n")
            for key, value in details.items():
                display_text.insert(tk.END, f"   {key}: {value}\n")
            display_text.insert(tk.END, "-"*30 + "\n")
    else:
        display_text.insert(tk.END, "No contacts found.\n")

def search_contact():
    name = name_entry.get()
    if name in contacts:
        contact = contacts[name]
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

        phone_entry.insert(0, contact["Phone"])
        email_entry.insert(0, contact["Email"])
        address_entry.insert(0, contact["Address"])
        messagebox.showinfo("Found", f"Details of '{name}' loaded.")
    else:
        messagebox.showerror("Not Found", f"No contact found with name '{name}'.")

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        clear_entries()
        messagebox.showinfo("Deleted", f"'{name}' removed from contacts.")
    else:
        messagebox.showerror("Error", f"No contact found with name '{name}'.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI
window = tk.Tk()
window.title("Contact Book")
window.geometry("450x500")
window.config(bg="#f9f9f9")

# Labels & Entries
tk.Label(window, text="Name:", bg="#f9f9f9").pack()
name_entry = tk.Entry(window, width=40)
name_entry.pack(pady=2)

tk.Label(window, text="Phone:", bg="#f9f9f9").pack()
phone_entry = tk.Entry(window, width=40)
phone_entry.pack(pady=2)

tk.Label(window, text="Email:", bg="#f9f9f9").pack()
email_entry = tk.Entry(window, width=40)
email_entry.pack(pady=2)

tk.Label(window, text="Address:", bg="#f9f9f9").pack()
address_entry = tk.Entry(window, width=40)
address_entry.pack(pady=2)

# Buttons
tk.Button(window, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white", width=20).pack(pady=5)
tk.Button(window, text="Search Contact", command=search_contact, bg="#2196F3", fg="white", width=20).pack(pady=5)
tk.Button(window, text="Delete Contact", command=delete_contact, bg="#f44336", fg="white", width=20).pack(pady=5)
tk.Button(window, text="View All Contacts", command=view_contacts, bg="#FF9800", fg="white", width=20).pack(pady=5)

# Display area
display_text = tk.Text(window, height=10, width=50)
display_text.pack(pady=10)

window.mainloop()