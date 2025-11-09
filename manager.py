
# HabitManager with streaks and persistence

import os
import json
from typing import List, Optional
from habit import Habit
from pet import Pet
from storage import load_json, save_json

class HabitManager:
    """ Manages habits and pets, handles persistence and core operations."""
    def __init__(self, habit_file="data/habit.json", pet_file="data/pet.json"):
        self.habit_file = habit_file
        self.pet_file = pet_file
        self.habits: List[Habit] = []
        self.pets: List[Pet] = []
        self.load_data()

    def load_data(self):
        """ Loads habits and pets from JSON files. """
        habit_data = load_json(self.habit_file)
        pet_data = load_json(self.pet_file)

    def save_data(self):
        """ Saves habits and pets to JSON files. """
        save_json(self.habit_file, [h.to_dict() for h in self.habits])
        save_json(self.pet_file, [p.to_dict() for p in self.pets])

    def create_habit(self, name:str, periodicity:str, description: str, pet: Pet):
        """ Creates a new habit and links it to a pet. """
        habit = Habit(name, periodicity, pet.nickname, description)
        self.habits.append(habit)
        self.pets.append(pet)
        self.save_data()

    def delete_habit(self, name:str):
        """ Deletes a habit and frees the associated pet. """
        self.habits = [h for h in self.habits if h.name != name]
        self.pets = [p for p in self.pets if p.nickname != name]
        self.save_data()

    def complete_habit(self, name:str):
        """ Marks a habit as completed and updates the pet's status."""
        habit = self.get_habit(name)
        if habit:
            habit.add_checkoff()
            pet = self.get_pet(habit.pet_name)
            if pet:
                pet.update_on_completion()
            self.save_data()

    def get_habit(self, name:str) -> Optional[Habit]:
        """ Retrieves a habit by name. """
        return next((h for h in self.habits if h.name == name), None)
    
    def get_pet(self,nickname:str) -> Optional[Pet]:
        """ Retrieves a pet by nickname."""
        return next((p for p in self.pets if p.nickname == nickname), None)
    
    def view_habit_list(self) -> List[str]:
        """ Returns a formatted list of habits sorted by periodicity and creation date. """
        sorted_habits = sorted(self.habits, key=lambda h: (h.periodicity, h.created_at))
        habit_list = []
        for habit in sorted_habits:
            habit_list.append(
                f"{habit.name} — {habit.periodicity} | Created: {habit.created_at.strftime('%Y-%m-%d')} | Pet: {habit.pet_name}"
                )
        return habit_list
    
    def list_pets(self) -> List[Pet]:
        """ Returns all pets. """
        return self.pets
    
    def view_streaks(self) -> List[str]:
        """ Returns a formatted list of habits sorted by the longest streak, descending """
        sorted_habits = sorted(self.habits, key = lambda h: h.longest_streak(), reverse=True)
        streaks = []
        for habit in sorted_habits:
            streaks.append(
                f"{habit.name} ({habit.periodicity})- Current Streak: {habit.current_streak()} | Longest: {habit.longest_streak()}"
            )
        return streaks

    def exit_and_save(self):
        """ Saves all data and exits the program. """
        self.save_data()
        print("Progress saved. Exiting program!")
        exit(0)
        