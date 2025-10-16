
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from habit import Habit
from datetime import datetime, timedelta


def test_add_checkoff_daily():

    habit = Habit("Read", "daily", "Whiskers", "Read a book daily")
    habit.add_checkoff()
    habit.add_checkoff()  # Same day, should be ignored
    assert len(habit.checkoffs) == 1


def test_streak_calculation_daily():
    habit = Habit("Water plants", "daily", "Bongo", "Keep plants hydrated")

    base_date = datetime(2025, 10, 8, 9, 0)
    for i in range(3):
        habit.add_checkoff(base_date - timedelta(days=i))

    assert habit.current_streak() == 3
    assert habit.longest_streak() == 3