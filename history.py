
# Initialize an empty history list
history = []

def add_entry(entry):
    """Add an entry to the history."""
    history.append(entry)

def get_history():
    """Retrieve the current history."""
    return history

def delete_last_entry():
    """Delete the last entry in the history and return it."""
    if history:
        return history.pop()
    return None

def reset_history():
    """Reset the history to an empty list."""
    global history
    history = []
