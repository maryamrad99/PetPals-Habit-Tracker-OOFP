
# 🐾 PetPals Habit Tracker App 🐾

A **Python-based CLI habit tracker** that gamifies building habits with virtual pets.  
Each habit is paired with a pet — completing habits increases your pet’s happiness and XP, while missing habits lowers happiness and breaks streaks.

---

## What is PetPals?

PetPals is a **command-line application** written in **Python** using **object-oriented design (OOP)**.  
It helps users stay consistent with their daily or weekly habits while having virtual pets that grow as does your progress.

### Features
- Create, complete, and delete habits
- Assign a pet (emoji:🐱 🐰 🦖 🐶 🐸) to each habit; pets gain XP, happiness, and levels
- Track streaks and pet happiness with a leaderboard
- Level up pets with experience points
- View analytics like:
  - Longest streak overall
  - Happiest pet
  - Filter by periodicity
- All data saved in JSON for persistence
- Both CLI (cli.py) and GUI (gui.py) frontends
- Unit tested with pytest

---

## Installation & Running

1. **Clone the repo:**
   ```bash
   git clone https://github.com/maryamrad99/PetPals-Habit-Tracker-OOFP.git
   cd PetPals-Habit-Tracker-OOFP
   ```

2. **Create and activate a virtual environment:**
- macOS/Linux: 
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
- Windows: 
   ```bash
   python -m venv env
   .\env\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the CLI app:**
   ```bash
   python cli.py
   ```
 Use the menu options to: 
   - Add a new habit with a pet
   - Complete habits to increase streaks and pet happiness
   - View streaks and analytics
   - Remove habits
   
or 

5. **Run GUI:**
   ```bash
   python gui.py
   ```

6. **Run the test:**
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