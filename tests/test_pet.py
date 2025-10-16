
import sys 
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from pet import Pet

def test_pet_initial_state():
    pet = Pet(species="Kitten", nickname="Whiskers", emoji="🐱")
    assert pet.species == "Kitten"
    assert pet.nickname == "Whiskers"
    assert pet.emoji == "🐱"
    assert pet.happiness == 50
    assert pet.level == 1
    assert pet.experience == 0
    assert pet.mood() == "Content 🙂"

def test_pet_update_on_completion():
    pet = Pet(species="Puppy", nickname="Bongo", emoji="🐶")
    pet.update_on_completion()
    assert pet.happiness == 55
    assert pet.experience == 10
    assert pet.level == 1  # Not enough XP to level up yet

def test_pet_level_up_logic():
    pet = Pet(species="Fox", nickname="Furry", emoji="🦊")
    for _ in range(5): # 5 completions x 10 XP = 50 XP
        pet.update_on_completion()
    assert pet.level == 2  # should level up to 2
    assert pet.experience == 0  # XP resets after leveling up

def test_pet_update_on_failure():
    pet = Pet(species="Dinosaur", nickname="Rexi", emoji="🦖")
    pet.happiness = 60
    pet.experience = 20
    pet.update_on_failure()
    assert pet.happiness == 50
    assert pet.experience == 15
    assert pet.level == 1  # Level should remain the same

def test_pet_mood_ranges():
    pet = Pet(species="Turtle", nickname="Shelly", emoji="🐢")

    pet.happiness = 85
    assert pet.mood() == "Joyful 😄!"
    
    pet.happiness = 65
    assert pet.mood() == "Content 🙂"

    pet.happiness = 30
    assert pet.mood() == "Grumpy 😠"

    pet.happiness = 10
    assert pet.mood() == "Sad 😢"