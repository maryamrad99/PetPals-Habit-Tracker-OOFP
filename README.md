
# 🐾 PetPals Habit Tracker App 🐾

A **Python-based CLI habit tracker** that gamifies building habits with virtual pets.  
Each habit is paired with a pet — completing habits increases your pet’s happiness and XP, while missing habits lowers happiness and breaks streaks.

---

## What is PetPals?

PetPals is a **command-line application** written in **Python** using **object-oriented design (OOP)**.  
It helps users stay consistent with their daily or weekly habits while having virtual pets that grow as does your progress.

### Features
- Create, complete, and delete habits
- Choose a pet emoji (🐱 🐰 🦖 🐶 🐸) to pair with each habit
- Track streaks and pet happiness
- Level up pets with experience points
- View analytics like:
  - Longest streak overall
  - Happiest pet
- All data saved in JSON for persistence

---

## Installation & Running

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Run the CLI app:**
   ```bash
   python3 cli.py
   ```

4.  Use the menu options to: 
   - Add a new habit with a pet
   - Complete habits to increase streaks and pet happiness
   - View streaks and analytics
   - Remove habits
   

5. **Run the test:**
   ```bash
   pytest -q
   ```
Tests include:
- Habit streak calculations
- Pet happiness and leveling system
- Analytics (filtering, longest streak, happiest pet)
- Data persistence (save/load JSON)

---

## Technologies Used
- Language: Python 3.12
- Libraries: *pytest, json, datetime, os, random*
- Storage: JSON files (for habits, pets, and events)
- Paradigm: Object-Oriented Programming (OOP)
- Interface: Command-Line Interface (CLI)
- Testing: Automated with *pytest*

--- 