import tkinter as tk  
from tkinter import messagebox  
import string  
import secrets  

def generate_password():  
    try:  
        length = int(length_entry.get())  
        if length < 4:  
            messagebox.showwarning("Warning", "Password length should be at least 4.")  
            return  

        all_chars = string.ascii_letters + string.digits + string.punctuation  

        password = [  
            secrets.choice(string.ascii_lowercase),  
            secrets.choice(string.ascii_uppercase),  
            secrets.choice(string.digits),  
            secrets.choice(string.punctuation)  
        ]  

        password += [secrets.choice(all_chars) for _ in range(length - 4)]  
        secrets.SystemRandom().shuffle(password)  

        password_entry.delete(0, tk.END)  
        password_entry.insert(0, "".join(password))  

    except ValueError:  
        messagebox.showerror("Error", "Please enter a valid number.")  

def toggle_password():  
    if password_entry.cget("show") == "*":  
        password_entry.config(show="")  
        toggle_btn.config(text="Hide")  
    else:  
        password_entry.config(show="*")  
        toggle_btn.config(text="Show")  

root = tk.Tk()  
root.title("Password Generator")  
root.geometry("360x320")  

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)  

tk.Label(root, text="Password Length").pack()  
length_entry = tk.Entry(root, width=10, font=("Arial", 12))  
length_entry.pack()  
length_entry.insert(0, "12")  

tk.Button(  
    root,  
    text="Generate Password",  
    command=generate_password,  
    bg="#2196f3",  
    fg="white",  
    font=("Arial", 10, "bold")  
).pack(pady=15)  

tk.Label(root, text="Generated Password").pack()  

password_entry = tk.Entry(root, width=25, font=("Courier", 14), show="*")  
password_entry.pack(pady=5)  

toggle_btn = tk.Button(root, text="Show", command=toggle_password)  
toggle_btn.pack()  

root.mainloop()  
