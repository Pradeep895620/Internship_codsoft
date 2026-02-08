import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_all():
    tasks_listbox.delete(0, tk.END)

# --- UI Setup ---
root = tk.Tk()
root.title("CodSoft Task 1: To-Do List")
root.geometry("400x450")

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, font=('Arial', 14), width=20)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task, bg="#4caf50", fg="white")
add_button.pack(side=tk.LEFT)

# Task List Display
tasks_listbox = tk.Listbox(root, font=('Arial', 12), width=40, height=10)
tasks_listbox.pack(pady=10, padx=20)

# Action Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="#f44336", fg="white")
delete_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_all, bg="#2196f3", fg="white")
clear_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
