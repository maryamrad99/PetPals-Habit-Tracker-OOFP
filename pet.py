
# Pet class with emoji, happiness, experience, and level

from typing import Optional

class Pet:
    """ 
    Represents a virtual pet linked to a habit. Tracks happiness, experience, and level.
    """

    def __init__(self, species: str, nickname: str, emoji: str):
        self.species = species
        self.nickname = nickname
        self.emoji = emoji  # User-selects emoji based on their own preference, like 🐱, 🐰, 🦖, 🐶, 🐸, etc
        self.happiness = 50  #Ranges from 0 to 100
        self.experience = 0  # Total experience points, user can gain experince when checking off habits
        self.level = 1  # Level increases based on experience points

    def update_on_completion(self):
        """ Boosts pet stats when a habit is completed. """

        self.happiness = min(100, self.happiness + 5)  
        self.experience += 10
        self.check_level_up()

    def update_on_failure(self):
        """ Decreases pet stats when a habit is failed to complete during its time period. """

        self.happiness = max(0, self.happiness - 10)
        self.experience = max(0, self.experience - 5)
        self.check_level_up()

    def check_level_up(self):
        """ Levels up the pet based on the experience points. """

        required_xp = self.level * 50  # Ex: Level 1 to level 2 requires 50 XP, level 2 to 3 requires 100 XP, etc.
        if self.experience >= required_xp:
            self.level += 1
            self.experience = 0  # Resets XP after leveling up

    def mood(self) -> str:
        """ Returns a mood description based on happiness score. """

        if self.happiness >= 80:
            return "Joyful 😄!"
        elif self.happiness >= 50:
            return "Content 🙂"
        elif self.happiness >= 20:
            return "Grumpy 😠"
        else:
            return "Sad 😢"
        
    def to_dict(self) -> dict:
        """ Serializes the pet to a dictionary for JSON storage. """
        return {
            "species": self.species,
            "nickname": self.nickname,
            "emoji": self.emoji,
            "happiness": self.happiness,
            "experience": self.experience,
            "level": self.level
        }
    
    @staticmethod
    def from_dict(data: dict) -> "Pet":
        """ Deserializes a pet from a dictionary. """
        
        pet = Pet(
            species = data["species"],
            nickname = data["nickname"],
            emoji = data.get("emoji")  # No default emoji, emoji must be provided
        )
        pet.happiness = data.get("happiness", 50)
        pet.experience = data.get("experience", 0)
        pet.level = data.get("level", 1)
        return pet
