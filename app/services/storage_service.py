import json 
from pathlib import Path

path = Path(__file__).parent.parent.parent / "data" / "students.json"

def load_students():
    try:
        with open(path, 'r') as file:
            content = json.load(file)
    except FileNotFoundError as e:
        content = []
        print(f"Error: {e}. File was not found")
    except json.JSONDecodeError as e:
        content = []
        print(f"Error: {e}. File is empty or not in valid JSON format")

    return content

def save_students(students):
    try:
        with open(path , 'w') as file:
             json.dump(students, file, indent=4)
    except TypeError as e:
        print(f"Error: {e}. Cannot be converted to JSON")
    except Exception as e:
        print(f"Error: {e}. Could not save students to file.")