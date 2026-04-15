import tkinter as tk
from tkinter import messagebox
import json

tasks = []

# program

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

def refresh():
    listbox.delete(0, tk.END)
    for t in tasks:
        listbox.insert(tk.END, f"{t['task']} ({t['priority']})")

def add():
    task = entry.get().strip()
    priority = priority_var.get()
    if not task:
        messagebox.showwarning("Error", "Type a task first :)")
        return
    tasks.append({"task": task, "priority": priority})
    save_tasks()
    refresh()
    entry.delete(0, tk.END)

def complete():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Error", "Select a task first :)")
        return
    index = selected[0]
    tasks.pop(index)
    save_tasks()
    refresh()

# gui
root = tk.Tk()
root.title("General Task Organizer")
root.geometry("500x400")
root.configure(bg="#E4E2D2")


left_frame = tk.Frame(root, bg="#EBBF87")
left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")


right_frame = tk.Frame(root, bg="#936046")
right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")


tk.Label(left_frame, text="TASK NAME:",
         bg="#EBBF87", fg="#5a3e2b",
         font=("Helvetica", 9, "bold")).grid(row=0, column=0, sticky="w")

entry = tk.Entry(left_frame,
                 bg="#E4E2D2",
                 fg="#5a3e2b",
                 insertbackground="#5a3e2b")
entry.grid(row=0, column=1, pady=5)


tk.Label(left_frame, text="PRIORITY:",
         bg="#EBBF87", fg="#5a3e2b",
         font=("Helvetica", 9, "bold")).grid(row=1, column=0, sticky="w")

priority_var = tk.StringVar(value="Medium")

priority_menu = tk.OptionMenu(left_frame, priority_var, "High", "Medium", "Low")
priority_menu.config(bg="#9A4C41",
                     fg="#E4E2D2",
                     activebackground="#7f3b32",
                     activeforeground="#E4E2D2",
                     font=("Helvetica", 10, "bold"),
                     highlightthickness=0)

priority_menu.grid(row=1, column=1, pady=5, sticky="ew")

btn_style = {"width": 15, "pady": 5}
tk.Button(left_frame, text="ADD",
          command=add,
          bg="#936046",
          fg="#E4E2D2",
          activebackground="#7a4f38",
          activeforeground="#E4E2D2",
          width=15, pady=5).grid(row=2, column=0, columnspan=2, pady=10)

tk.Button(left_frame, text="REFRESH",
          command=refresh,
          bg="#936046",
          fg="#E4E2D2",
          activebackground="#7a4f38",
          activeforeground="#E4E2D2",
          width=15, pady=5).grid(row=3, column=0, columnspan=2, pady=5)

tk.Button(left_frame, text="COMPLETE",
          command=complete,
          bg="#936046",
          fg="#E4E2D2",
          activebackground="#7a4f38",
          activeforeground="#E4E2D2",
          width=15, pady=5).grid(row=4, column=0, columnspan=2, pady=5)

tk.Button(left_frame, text="EXIT",
          command=root.quit,
          bg="#9A4C41",
          fg="#E4E2D2",
          activebackground="#7f3b32",
          activeforeground="#E4E2D2",
          width=10).grid(row=6, column=0, columnspan=2, pady=30)
listbox = tk.Listbox(right_frame, width=30, height=15)
listbox.pack(side="left", fill="both")

scrollbar = tk.Scrollbar(right_frame)
scrollbar.pack(side="right", fill="y")
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.grid_columnconfigure(1, weight=1)

load_tasks()
refresh()
root.mainloop()
