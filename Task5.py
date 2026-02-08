import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# File to store data
DATA_FILE = "contacts.json"

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("CodSoft Contact Book")
        self.root.geometry("500x500")
        self.contacts = self.load_data()

        # UI Elements
        tk.Label(root, text="Contact Management System", font=("Arial", 16, "bold")).pack(pady=10)

        # Input Fields
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        
        frame = tk.Frame(root)
        frame.pack(pady=10)
        
        tk.Label(frame, text="Name:").grid(row=0, column=0)
        tk.Entry(frame, textvariable=self.name_var).grid(row=0, column=1, padx=5)
        
        tk.Label(frame, text="Phone:").grid(row=1, column=0)
        tk.Entry(frame, textvariable=self.phone_var).grid(row=1, column=1, padx=5)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Add Contact", command=self.add_contact, bg="green", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete_contact, bg="red", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Search", command=self.search_contact).pack(side=tk.LEFT, padx=5)

        # Listbox
        self.listbox = tk.Listbox(root, width=60)
        self.listbox.pack(pady=10, padx=10)
        
        self.update_listbox()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        return {}

    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.contacts, f)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        if name and phone:
            self.contacts[name] = {"phone": phone}
            self.save_data()
            self.update_listbox()
            self.name_var.set("")
            self.phone_var.set("")
        else:
            messagebox.showwarning("Error", "All fields are required")

    def update_listbox(self, filter_contacts=None):
        self.listbox.delete(0, tk.END)
        data = filter_contacts if filter_contacts is not None else self.contacts
        for name, info in data.items():
            self.listbox.insert(tk.END, f"{name} - {info['phone']}")

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter name to search:")
        if query:
            results = {k: v for k, v in self.contacts.items() if query.lower() in k.lower()}
            self.update_listbox(results)

    def delete_contact(self):
        try:
            selected = self.listbox.get(self.listbox.curselection())
            name = selected.split(" - ")[0]
            del self.contacts[name]
            self.save_data()
            self.update_listbox()
        except:
            messagebox.showwarning("Error", "Select a contact to delete")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
