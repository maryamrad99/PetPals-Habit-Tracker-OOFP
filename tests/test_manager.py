
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from manager import HabitManager
from habit import Habit
from pet import Pet
from datetime import datetime, timedelta


def test_create_and_link_to_pet():
    manager = HabitManager(habit_file= "tests/mock_habit.json", pet_file="tests/mock_pet.json")
    pet = Pet("Kitten", "Whiskers","😺" )
    manager.create_habit("Read", "daily", "Read a book daily", pet)

    habit = manager.get_habit("Read")
    assert habit is not None
    assert habit.pet_name == "Whiskers"

    linked_pet = manager.get_pet("Whiskers")
    assert linked_pet is not None
    assert linked_pet.species == "Kitten"

def test_complete_habit_updates_pet():
    manager = HabitManager(habit_file="tests/mock_habit.json", pet_file="tests/mock_pet.json")
    pet = Pet("Puppy", "Bongo", "🐶")
    manager.create_habit("Water plants", "daily", "Keep plants hydrated", pet)

    manager.complete_habit("Water plants")

    habit = manager.get_habit("Water plants")
    assert len(habit.checkoffs) == 1

    updated_pet = manager.get_pet("Bongo")
    assert updated_pet.experience == 10
    assert updated_pet.happiness == 55

def test_view_streaks_formatting():
    manager = HabitManager(habit_file="tests/mock_habit.json", pet_file="tests/mock_pet.json")
    pet = Pet("Fox", "Furry", "🦊")
    manager.create_habit("Stretch", "daily", "Stretch every morning", pet)

    habit = manager.get_habit("Stretch")
    for i in range(3):
        habit.add_checkoff(datetime.now() - timedelta(days=i))

    streaks = manager.view_streaks()
    assert any("Stretch" in s and "Current Streak: 3" in s for s in streaks)

