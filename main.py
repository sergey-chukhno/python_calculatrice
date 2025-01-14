import os
import history  # Import the history module

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_result():
    """Calculate the result based on the current history."""
    hist = history.get_history()
    if not hist:
        return 0
    
    result = float(hist[0])
    current_operator = None

    for entry in hist[1:]:
        if entry in ['+', '-', '*', '/']:
            current_operator = entry
        else:
            try:
                num = float(entry)
                if current_operator == '+':
                    result += num
                elif current_operator == '-':
                    result -= num
                elif current_operator == '*':
                    result *= num
                elif current_operator == '/':
                    if num == 0:
                        raise ZeroDivisionError("Division by zero is not allowed.")
                    result /= num
            except ValueError:
                continue
    return result

def calculator():
    print('Welcome!')
    print('List of available operations: +, -, *, /, =')
    print('Press "space" to exit')
    print('Press "d" to delete the last entry, "z" to reset the result to zero, or "h" to show history')

    # Ask for the first number
    while True:
        first_input = input("Enter the first number, or press 'h' to show history, 'd' to delete, or 'space' to exit: ").strip()
        
        if first_input == '':
            print('Exiting the calculator. Goodbye!')
            return
        elif first_input == 'h':
            if history.get_history():
                print("Calculation History: " + " ".join(history.get_history()))
            else:
                print("History is empty.")
            continue
        elif first_input == 'd':
            print("List is empty. Nothing to delete.")
            continue
        
        try:
            first_number = float(first_input)
            history.add_entry(first_input)  # Add the first number to history
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    clear_screen()

    while True:
        try:
            hist = history.get_history()
            if hist and hist[-1] in ['+', '-', '*', '/']:
                prompt = "Enter the next number, 'h' to show history, or 'd' to delete: "
            else:
                prompt = "Enter an operator (+, -, *, /, =), 'd' to delete, 'z' to reset, 'h' to show history, or press 'space' to exit: "

            user_input = input(prompt).strip()

            if user_input == '':
                print('Exiting the calculator. Goodbye!')
                return

            if user_input == '=':
                if not hist:
                    print("Nothing to calculate. Please enter numbers first.")
                    continue
                try:
                    result = calculate_result()
                    print(f"The result is: {result}")
                    continue  # Return to ask for a new operator after displaying the result
                except ZeroDivisionError as e:
                    print(e)
                    continue  # Handle division by zero and return to ask for operator

            if user_input == 'h':
                if hist:
                    print("Calculation History: " + " ".join(hist))
                else:
                    print("History is empty.")
                continue

            if user_input == 'd':
                last_entry = history.delete_last_entry()
                if last_entry:
                    print(f"Deleted last entry: {last_entry}")
                    if not history.get_history():
                        print("History is now empty. Enter the first number.")
                else:
                    print("No entries to delete.")
                continue

            if user_input == 'z':
                history.reset_history()
                print("Result reset to zero.")
                while True:
                    first_input = input("Enter the first number, or press 'h' to show history, 'd' to delete, or 'space' to exit: ").strip()
                    if first_input == '':
                        print('Exiting the calculator. Goodbye!')
                        return
                    elif first_input == 'h':
                        print("History is empty.")
                        continue
                    elif first_input == 'd':
                        print("List is empty. Nothing to delete.")
                        continue
                    
                    try:
                        first_number = float(first_input)
                        history.add_entry(first_input)  # Add the first number to history
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                clear_screen()
                continue

            if user_input in ['+', '-', '*', '/']:
                if not hist or hist[-1] in ['+', '-', '*', '/']:
                    print("Cannot enter two consecutive operators. Please enter a number first.")
                else:
                    history.add_entry(user_input)
                continue

            try:
                num = float(user_input)
                history.add_entry(user_input)  # Add number to history
            except ValueError:
                print("Invalid input. Please try again.")

            clear_screen()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    calculator()
