from manager import HabitManager
import manager
from pet import Pet
from analytics import (
    list_all_habits,
    filter_by_periodicity,
    longest_streak_all,
    happiest_pet
)

def run_cli():
    manager = HabitManager()

    while True:
        print("\n 🐾 Welcome to PetPals Habit Tracker 🐾")
        print("1. Create a new habit")
        print("2. View habit list")
        print("3. Complete a habit")
        print("4. View streak leaderboard")
        print("5. View analytics")
        print("6. Delete a habit")
        print("7. Exit and save")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            name = input("Habit name: ")
            periodicity = input("Periodicity (hourly/daily/weekly/monthly): ")
            description = input("Description: ")
            species = input("Pet species: ")
            nickname = input("Pet nickname: ")
            emoji = input("Choose a pet emoji (e.g. 🐶 🐱 🐹 🐢 🦖 🐡 🐄 🦘): ")
            pet = Pet(species, nickname, emoji)
            manager.create_habit(name, periodicity, description, pet)
            print(f"Habit '{name}' created with pet {emoji}!")

        elif choice == "2":
            habits = manager.view_habit_list()
            print("\n Your habits: ")
            if habits:
                for h in habits:
                    print(f" - {h}")
            else:
                print("You have no habits yet.")

        elif choice == "3":
            if not manager.habits:
                print("\n You haven't created any habits yet! ")
            else:
                name = input("Enter habit name to complete: ").strip()
                manager.complete_habit(name)
            print(f"\n Habit '{name}' marked as completed!")


        elif choice == "4":
            streaks = manager.view_streaks()
            print("\n Streaks LeaderBoard: ")
            if streaks:
                for s in streaks:
                    print(f" - {s}")
            else:
                print("No streaks to show yet! Start building one today.")

        elif choice == "5":
            print("\n Analytics:")

            all_habits = list_all_habits(manager.habits)
            if all_habits:
                print("All habits:", all_habits)
                period = input("Filter habits by periodicity (hourly/daily/weekly/monthly): ")
                filtered = filter_by_periodicity(manager.habits, period)
                print("Filtered habits:", filtered if filtered else "No habits match that periodicity.")
                print("Longest streak:", longest_streak_all(manager.habits))
                print("Happiest pet:", happiest_pet(manager.pets))
            else:
                print("No habits or pets to analyze yet!")

        elif choice == "6":
            name = input("Enter habit name to delete: ").strip()
            habit = manager.get_habit(name)
            if habit:
                manager.delete_habit(name)
                print(f"Habit '{name}' deleted.")
            else:
                print(f"Habit '{name}' not found.")


        elif choice == "7":
            manager.exit_and_save()

        else:
            print("\n Invalid choice. Please select a number from 1 to 7.")

if __name__ == "__main__":
    run_cli()


