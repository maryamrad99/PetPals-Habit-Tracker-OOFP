
import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from storage import load_json

def test_load_files():
    # Define paths to your JSON files
    base_path = os.path.join(os.path.dirname(__file__), "..", "data")
    habits_file = os.path.join(base_path, "habit.json")
    pets_file = os.path.join(base_path, "pet.json")

    # Load data
    habits_data = load_json(habits_file)
    pets_data = load_json(pets_file)

    # Print nicely for verification
    print("\n HABITS DATA LOADED SUCCESSFULLY:")
    print(json.dumps(habits_data, indent=4, ensure_ascii=False))

    print("\n PETS DATA LOADED SUCCESSFULLY:")
    print(json.dumps(pets_data, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    test_load_files()


