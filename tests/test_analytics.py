
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from analytics import (
    list_all_habits,
    filter_by_periodicity,
    longest_streak_all,
    longest_streak_for,
    happiest_pet
)
from habit import Habit
from pet import Pet
from datetime import datetime, timedelta

def test_list_all_habits():
    h1 = Habit("Read", "daily", "Whiskers", "Read books")
    h2 = Habit("Stretch", "weekly", "Bongo", "Stretch weekly")
    habits = [h1, h2]
    names = list_all_habits(habits)
    assert names == ["Read", "Stretch"]

def test_filter_by_periodicity():
    h1 = Habit("Read", "daily", "Whiskers", "Read books")
    h2 = Habit("Stretch", "weekly", "Bongo", "Stretch weekly")
    h3 = Habit("Journal", "daily", "Flick", "Write thoughts")
    habits = [h1, h2, h3]
    filtered = filter_by_periodicity(habits, "daily")
    assert filtered == ["Read", "Journal"]

def test_longest_streak_all():
    h1 = Habit("Read", "daily", "Whiskers", "Read books")
    h2 = Habit("Stretch", "daily", "Bongo", "Stretch daily")
    for i in range(5):
        h1.add_checkoff(datetime.now() - timedelta(days=i))
    for i in range(3):
        h2.add_checkoff(datetime.now() - timedelta(days=i))
    result = longest_streak_all([h1, h2])
    assert result.startswith("Read - 5")

def test_longest_streak_for():
    h = Habit("Journal", "daily", "Flick", "Write thoughts")
    for i in range(4):
        h.add_checkoff(datetime.now() - timedelta(days=i))
    streak = longest_streak_for(h)
    assert streak == 4

def test_happiest_pet():
    p1 = Pet("cat", "Whiskers", "😺")
    p2 = Pet("dog", "Bongo", "🐶")
    p1.happiness = 90
    p2.happiness = 60
    result = happiest_pet([p1, p2])
    assert result.startswith("Whiskers 😺")