
# Habit class with flexible periodicity and streak logic

from datetime import datetime, timedelta
from typing import List, Optional

class Habit:
    """
    Represents a user-defined habit with periodicity and completion tracking.
    """

    def __init__(self, name: str, periodicity: str, pet_name: str, description: str):
        self.name = name
        self.periodicity = periodicity.lower()  # 'hourly', 'daily', 'weekly', 'monthly'
        self.pet_name = pet_name
        self.description = description
        self.created_at = datetime.now()
        self.checkoffs: List[datetime] = []

    def add_checkoff(self, date: Optional[datetime] = None):
        """
        Records a habit completion. Only one checkoff per habit period(daily/weekly/hourly) is allowed.
        """

        date = date or datetime.now()
        if not self.already_checked(date):
            self.checkoffs.append(date)

    def already_checked(self, date:datetime) -> bool:
        """
        Checks if a habit was already completed for the given period.
        """

        for d in self.checkoffs:
            if self.periodicity == "hourly" and d.hour == date.hour and d.date() == date.date():
                return True
            elif self.periodicity == "daily" and d.date() == date.date():
                return True
            elif self.periodicity == "weekly" and d.isocalendar()[1] == date.isocalendar()[1] and d.year == date.year:
                return True
            elif self.periodicity == "monthly" and d.month == date.month and d.year == date.year:
                return True
        return False
    
    def current_streak(self) -> int:
        """
        Calculates the current streak based on consecutive completions.
        """

        if not self.checkoffs:
            return 0
        sorted_dates = sorted(set(self.normalized_dates()), reverse=True)
        streak = 1
        for i in range(1, len(sorted_dates)):
            if self.is_consecutive(sorted_dates[i - 1], sorted_dates[i]):
                streak += 1
            else:
                break
        return streak
    
    def longest_streak(self) -> int:
        """
        Calculates the longest streak from all checkoffs.
        """

        if not self.checkoffs:
            return 0
        sorted_dates = sorted(set(self.normalized_dates()))
        longest = current = 1
        for i in range(1, len(sorted_dates)):
            if self.is_consecutive(sorted_dates[i - 1], sorted_dates[i]):
                current += 1
                longest = max(longest, current)
            else:
                current = 1
        return longest
    
    def normalized_dates(self) -> List[datetime]:
        """
        Normalizes checkoff timestamps to the start of their respective periods.
        """

        normalized = []
        for dt in self.checkoffs:
            if self.periodicity == "hourly":
                normalized.append(dt.replace(minute=0, second=0, microsecond=0))
            elif self.periodicity == "daily":
                normalized.append(dt.replace(hour=0, minute=0, second=0, microsecond=0))
            elif self.periodicity == "weekly":
                start_of_week = dt - timedelta(days=dt.weekday())
                normalized.append(start_of_week.replace(hour=0, minute=0, second=0, microsecond=0))
            elif self.periodicity == "monthly":
                normalized.append(dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0))
        return normalized
    
    def is_consecutive(self, d1: datetime, d2: datetime) -> bool:
        """
        Checks if two normalized dates are consecutive based on the periodicity.
        """

        if self.periodicity == "hourly":
            return (d2 - d1) == timedelta(hours=1)
        elif self.periodicity == "daily":
            return abs((d1 - d2).days) == 1
        elif self.periodicity == "weekly":
            return (d2 - d1) == timedelta(weeks=1)
        elif self.periodicity == "monthly":
            return (d2.month - d1.month == 1 and d1.year == d2.year) or \
                   (d1.month == 1 and d2.month == 12 and d1.year - d2.year == 1)
        return False
    
    def to_dict(self) -> dict:
        """
        Serializes the habit to a dictionary for JSON storage.
        """

        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "pet_name": self.pet_name,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "checkoffs": [dt.isoformat() for dt in self.checkoffs]
        }
    
    @staticmethod
    def from_dict(data: dict) -> "Habit":
        """
        Deserializes a habit from a dictionary.
        """
        
        habit = Habit(
            name=data["name"],
            periodicity=data["periodicity"],
            pet_name=data["pet_name"],
            description=data.get("description", ""),
        )
        habit.created_at = datetime.fromisoformat(data["created_at"])
        habit.checkoffs = [datetime.fromisoformat(dt) for dt in data.get("checkoffs", [])]
        return habit
