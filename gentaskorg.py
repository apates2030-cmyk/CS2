import tkinter as tk
from tkinter import messagebox
import json

tasks = []

# loading and saving
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except:
        tasks = []

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

# adding & priority 
def refresh():
    listbox.delete(0, tk.END)
    for t in tasks:
        listbox.insert(tk.END, f"{t['task']} ({t['priority']})")

def add():
    task = entry.get().strip()
    priority = priority_var.get()

    if not task:
        messagebox.showwarning("Type a task first :)")
        return

    tasks.append({"task": task, "priority": priority})
    save_tasks()
    refresh()
    entry.delete(0, tk.END)

def complete():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Select a task first :)")
        return

    index = selected[0]
    tasks.pop(index)

    save_tasks()
    refresh()

# gui
root = tk.Tk()
root.title("General Task Organizer")
root.geometry("500x550")

entry = tk.Entry(root)
entry.pack(pady=10)

priority_var = tk.StringVar(value="Medium")
tk.OptionMenu(root, priority_var, "High", "Medium", "Low").pack()

tk.Button(root, text="Add Task", command=add).pack(pady=5)
tk.Button(root, text="Complete Task", command=complete).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

listbox = tk.Listbox(root)
listbox.pack(fill="both", expand=True, pady=10)

# program
load_tasks()
refresh()

root.mainloop()
