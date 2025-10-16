
# Pure functions for streaks, filters, and pet stats

from typing import List
from habit import Habit
from pet import Pet

def list_all_habits(habits:List[Habit]) -> List[str]:
    """ Returns a list of all habit names."""

    return [habit.name for habit in habits]

def filter_by_periodicity(habits: List[Habit], period:str) -> List[str]:
    """ Filters habits by periodicity (e.g., 'hourly', 'daily', 'weekly', 'monthly') and returns their names ."""

    return [habit.name for habit in habits if habit.periodicity == period.lower()]

def longest_streak_all(habits: List[Habit]) -> str:
    """ Returns the name of the habit with the longest streak overall. """

    if not habits:
        return "No habits found."
    longest = max(habits, key=lambda h: h.longest_streak())
    return f"{longest.name} - {longest.longest_streak()} streaks"

def longest_streak_for(habit: Habit) -> int:
    """ Returns the longest streak for a specific habit. """

    return habit.longest_streak()

def happiest_pet(pets: List[Pet]) -> str:
    """ Returns the nickname and emoji of the happiest pet. """

    if not pets: 
        return " No pets found."
    happiest = max(pets, key=lambda p: p.happiness)
    return f"{happiest.nickname} {happiest.emoji} - Happiness : {happiest.happiness}"