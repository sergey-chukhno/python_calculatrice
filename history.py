
# Store history entries and the current ongoing calculation
history = []
current_entry = ""

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
        return history.pop()
    return None

def reset_history():
    """Clear the entire history and the current entry."""
    global history, current_entry
    history = []
    current_entry = ""
