
import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime

from manager import HabitManager
from pet import Pet
from analytics import (
    list_all_habits,
    filter_by_periodicity,
    longest_streak_all,
    happiest_pet,
)

# Initialize manager
manager = HabitManager()

# Styling
root = tk.Tk()
root.title("PetPals")
root.geometry("420x720")
root.configure(bg="#ab97c2")

BTN_BG = "#d0a8b8"
BTN_FG = "#000000"
BTN_BORDER = "#000000"
BOTTOM_BTN_BG = "#aa98ba"

pad_x = 18
pad_y = 12

# top date + small tagline
today = datetime.date.today().strftime("%B %d, %Y")
top_frame = tk.Frame(root, bg=root["bg"])
top_frame.pack(pady=(18, 6))
tk.Label(top_frame, text=f"📅 {today}", font=("Courier New", 19), bg=root["bg"], fg="#fff").pack()
tk.Label(top_frame, text="Small habits make big changes", font=("Courier New", 13, "italic"), bg=root["bg"], fg="#fff").pack()

# Header title
header_bg = root["bg"]
tk.Label(
    root,
    text="🐾 PetPals 🐾 \n Your Habit-Tracking Companion ",
    font=("Courier New", 20, "bold"),
    fg="#4d2585",
    bg=header_bg,
).pack(pady=(12, 6))

# Button grid
btn_frame = tk.Frame(root, bg=root["bg"])
btn_frame.pack(pady=20)

def make_pixel_btn(parent, text, command, width=20, height=2):
    """ Create a pixel-like style button for the UI. """
    btn = tk.Button(
        parent,
        text=text,
        command=command,
        font=("Courier New", 12, "bold"),
        bg=BTN_BG,
        fg=BTN_FG,
        relief="raised",
        bd=3,
        activebackground="#ffd1e8",
        width=width,
        height=height,
    )
    return btn


# Handlers 
def open_create_habit_modal():
    """ Opens a window that collects inputs, such as habit name, periodicity, description,
    pet species, pet nickname, and pet emoji, for creating a new habit. """
    modal = tk.Toplevel(root)
    modal.title("Create Habit")
    modal.geometry("360x380")
    modal.configure(bg="#2A184C")

    def create_entry(parent, placeholder):
        """ Creates and packs a single entry widget with placeholder text. """
        e = tk.Entry(parent, width=36, font=("Courier New", 11))
        e.insert(0, placeholder)
        e.pack(pady=6)
        return e

    tk.Label(modal, text="Create New Habit", font=("Courier New", 12, "bold"), bg=modal["bg"], fg="#fff").pack(pady=8)
    name_e = create_entry(modal, "Habit name")
    period_e = create_entry(modal, "Periodicity (hourly/daily/weekly/monthly)")
    desc_e = create_entry(modal, "Description")
    species_e = create_entry(modal, "Pet species")
    nickname_e = create_entry(modal, "Pet nickname")
    emoji_e = create_entry(modal, "Pet emoji (e.g. 🐶,🐱,🐭,🐹,🐰,etc)")

    def submit():
        """ Accepts input, creates a Pet, and calls on manager.create_habit.
        Then shows warnings or confirmation messages. """
        name = name_e.get().strip()
        period = period_e.get().strip()
        desc = desc_e.get().strip()
        species = species_e.get().strip()
        nick = nickname_e.get().strip()
        emoji = emoji_e.get().strip()
        if not all([name, period, desc, species, nick, emoji]):
            messagebox.showwarning("Missing", "Fill all fields")
            return
        pet = Pet(species, nick, emoji)
        manager.create_habit(name, period, desc, pet)
        messagebox.showinfo("Created", f"Habit '{name}' added")
        modal.destroy()

    # action buttons in the modal
    tk.Button(modal, text="Create", command=submit, bg="#ffd1e8", fg="#000", font=("Courier New", 11, "bold")).pack(pady=12)
    tk.Button(modal, text="Cancel", command=modal.destroy, bg="#b7a1d9", fg="#000", font=("Courier New", 10)).pack(pady=4)


def show_habits_list():
    """ Displays a read-only window listing all habits returned by manager.view_habit_list.
    If no habits exist, outputs that no habits are found. """
    habits = manager.view_habit_list()
    win = tk.Toplevel(root)
    win.title("Habits list")
    win.geometry("360x420")
    win.configure(bg="#3b2a56")
    tk.Label(win, text="Habits", font=("Courier New", 12, "bold"), bg=win["bg"], fg="#fff").pack(pady=8)
    listbox = tk.Listbox(win, width=50, height=18, font=("Courier New", 10))
    listbox.pack(pady=6)
    if habits:
        for h in habits:
            listbox.insert(tk.END, h)
    else:
        listbox.insert(tk.END, "No habits found.")


def complete_habit_prompt():
    """ Lets the user mark a habit as completed.
    Uses simpledialog to get user input and manager.complete_habit to register the completion. 
    If no habits created yet, it inform the user. """
    habits = manager.view_habit_list()
    if not habits:
        messagebox.showinfo("Complete Habit", "No habits available to complete.")
        return
    name = simpledialog.askstring("Complete Habit", "Enter habit name to mark complete:")
    if not name:
        return
    manager.complete_habit(name.strip())
    messagebox.showinfo("Completed", f"Habit '{name}' marked complete.")


def show_streaks():
    """ Gets streaks from manager.view_streaks and show them in a message box.
    If none exist, it inform the user. """
    streaks = manager.view_streaks()
    if not streaks:
        messagebox.showinfo("Streaks", "No streaks to show yet.")
        return
    messagebox.showinfo("Streak Leaderboard", "\n".join(streaks))


def show_analytics():
    """ Present all the analytics by calling helper functions from analytics module.
    Allows optional filtering by periodicity via simpledialog.
    Displays results in a message box. """
    if not manager.habits:
        messagebox.showinfo("Analytics", "No habits or pets to analyze yet!")
        return
    period = simpledialog.askstring("Filter", "Filter periodicity (hourly/daily/weekly/monthly):")
    filtered = filter_by_periodicity(manager.habits, period) if period else manager.habits
    longest = longest_streak_all(manager.habits)
    happy = happiest_pet(manager.pets)
    msg = f"All habits: {list_all_habits(manager.habits)}\n\nFiltered ({period}): {filtered if filtered else 'None'}\n\nLongest streak: {longest}\n\nHappiest pet: {happy}"
    messagebox.showinfo("Analytics", msg)


def remove_habit_prompt():
    """ Ask the user for a habit name to remove. Confirm the action and delegate to manager.delete_habit. """
    if not manager.habits:
        messagebox.showinfo("Remove Habit", "No habits to remove.")
        return
    name = simpledialog.askstring("Remove Habit", "Enter habit name to remove:")
    if not name:
        return
    confirm = messagebox.askyesno("Confirm", f"Delete habit '{name}'?")
    if confirm:
        manager.delete_habit(name.strip())
        messagebox.showinfo("Removed", f"Habit '{name}' removed.")


def exit_and_save():
    """ Save any persistent state via manager.exit_and_save, show confirmation, and exit the GUI. """
    manager.exit_and_save()
    messagebox.showinfo("Saved", "Progress saved. Exiting.")
    root.destroy()


# Six option buttons
btns = [
    ("Create Habit", open_create_habit_modal, 18),
    ("Habits list", show_habits_list, 18),
    ("Complete Habit", complete_habit_prompt, 18),
    ("Streaks", show_streaks, 18),
    ("Analytics", show_analytics, 18),
    ("Remove Habit", remove_habit_prompt, 18),
]

r = 0
c = 0
for (label, cmd, w) in btns:
    b = make_pixel_btn(btn_frame, label, cmd, width=w, height=2)
    b.grid(row=r, column=c, padx=pad_x, pady=pad_y)
    c += 1
    if c > 1:
        c = 0
        r += 1

# EXIT button
tk.Button(root, text="EXIT", command=exit_and_save, font=("Courier New", 12, "bold"), bg="#00d1b2", fg="#000000", width=34, height=2).pack(pady=22)

# run
root.mainloop()
