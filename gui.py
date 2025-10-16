
import tkinter as tk
from tkinter import messagebox
from manager import HabitManager
from pet import Pet

# Initialize manager
manager = HabitManager()

# GUI setup 
root = tk.Tk()
root.title("PetPals - Your Habit-Tracking Companion")
root.geometry("700x550")
root.configure(bg="#2f2f60")

# Load pixel-style font (fallback to Courier)
pixel_font = ("Courier New", 10)

# Habit listbox
habit_listbox = tk.Listbox(root, width=80, height=10, font=pixel_font)
habit_listbox.pack(pady=10)

# Header
tk.Label(root, text="🐾 PetPals - Your Habit-Tracking Companion 🐾", 
         font=("Courier New", 16, "bold"), fg="#bd93f9", bg="#1e1e2f").pack(pady=(20, 5))
import datetime
today = datetime.date.today().strftime("%B %d, %Y")
tk.Label(root, text=f"📅 Today: {today}", 
         font=("Courier New", 10), fg="#f8f8f2", bg="#1e1e2f").pack()
tk.Label(root, text="“Small habits make big changes.”", 
         font=("Courier New", 10, "italic"), fg="#f8f8f2", bg="#1e1e2f").pack(pady=(0, 10))

# ----------- Functions -----------

def refresh_habit_list():
    habit_listbox.delete(0, tk.END)
    habits = manager.view_habit_list()
    if habits:
        for h in habits:
            habit_listbox.insert(tk.END, h)
    else:
        habit_listbox.insert(tk.END, "No habits found. Add a new habit!")

def complete_selected_habit():
    selection = habit_listbox.curselection()
    if selection:
        habit_test = habit_listbox.get(selection[0])
        habit_name = habit_test.split(" - ")[0]
        manager.complete_habit(habit_name)
        messagebox.showinfo("Completed", f"Habit '{habit_name}' marked as complete!")
        refresh_habit_list()
    else:
        messagebox.showwarning("No Selection", "Please select a habit to complete.")

def add_habit():
    name = name_entry.get().strip()
    periodicity = period_entry.get().strip()
    species = species_entry.get().strip()
    nickname = nickname_entry.get().strip()
    emoji = emoji_entry.get().strip()

    if not all([name, periodicity, species, nickname, emoji]):
        messagebox.showwarning("Missing Info", "Please fill in all fields.")
        return

    pet = Pet(species, nickname, emoji)
    manager.create_habit(name, periodicity, f"{name} description", pet)
    messagebox.showinfo("Habit Added", f"Habit '{name}' with pet {emoji} added!")
    refresh_habit_list()

# ----------- Widgets -----------

# Title
tk.Label(root, text="🐾 PetPals Habit Tracker", font=("Courier New", 14, "bold"), fg="#bd93f9", bg="#1e1e2f").pack(pady=10)

# Habit list
habit_listbox = tk.Listbox(root, width=80, height=10, font=pixel_font, bg="#282a36", fg="#f8f8f2", selectbackground="#44475a")
habit_listbox.pack(pady=10)

# Complete button
tk.Button(root, text="Complete Selected Habit", command=complete_selected_habit, font=pixel_font, bg="#44475a", fg="#f8f8f2").pack(pady=5)

# Add habit section
tk.Label(root, text="Add New Habit", font=("Courier New", 12, "bold"), fg="#bd93f9", bg="#1e1e2f").pack(pady=10)

def create_entry(placeholder):
    entry = tk.Entry(root, width=40, font=pixel_font, bg="#282a36", fg="#f8f8f2", insertbackground="#f8f8f2")
    entry.insert(0, placeholder)
    entry.pack()
    return entry

name_entry = create_entry("Habit name")
period_entry = create_entry("Periodicity (hourly/daily/weekly/monthly)")
species_entry = create_entry("Pet species")
nickname_entry = create_entry("Pet nickname")
emoji_entry = create_entry("Pet emoji 🐶")

tk.Button(root, text="Add Habit", command=add_habit, font=pixel_font, bg="#44475a", fg="#f8f8f2").pack(pady=10)

# Initial load
refresh_habit_list()

# Run the GUI
root.mainloop()

