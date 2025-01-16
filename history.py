import os
import json

history_file = "history.json"  # Default history file name

history = []
current_entry = ""

# File handling functions
def load_history_from_file():
    """Load history from the JSON file."""
    global history
    if os.path.exists(history_file):
        with open(history_file, 'r') as file:
            try:
                history = json.load(file)
            except json.JSONDecodeError:
                history = []  # Reset if the file is corrupted
    else:
        history = []

def save_history_to_file():
    """Save the current history to the JSON file."""
    with open(history_file, 'w') as file:
        json.dump(history, file)


def open_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print(f"\nData from {filename}:")
            print(data)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def rename_history_file(new_name):
    """Rename the history file."""
    global history_file
    if os.path.exists(history_file):
        os.rename(history_file, new_name)
        history_file = new_name
    else:
        print("No history file found to rename.")

# Calculator functions
def add_to_current_entry(value):
    """Add a value (number/operator) to the ongoing calculation."""
    global current_entry
    current_entry += str(value)

def finalize_current_entry(result):
    """
    Finalize the current calculation as an entry in the history.
    Append 'result' to the entry and save it in history.
    """
    global current_entry, history
    current_entry += f" = {result}"
    history.append(current_entry)
    save_history_to_file()  # Save history to file after every update
    current_entry = str(result)  # Start the next calculation with the result

def delete_last_from_current_entry():
    """Delete the last character from the current ongoing entry."""
    global current_entry
    if current_entry:
        current_entry = current_entry[:-1]

def reset_current_entry():
    """Reset the current ongoing entry."""
    global current_entry
    current_entry = ""

def get_current_entry():
    """Retrieve the current ongoing calculation."""
    return current_entry

def get_history():
    """Retrieve the saved history."""
    return history

def delete_last_history_entry():
    """Delete the last entry in the history."""
    if history:
        entry = history.pop()
        save_history_to_file()  # Save after deletion
        return entry
    return None

def reset_history():
    """Clear the entire history and the current entry."""
    global history, current_entry
    history = []
    current_entry = ""
    save_history_to_file()  # Save the empty history to file

# Load history from file on startup
load_history_from_file()