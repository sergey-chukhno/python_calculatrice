import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_result(history):
    if not history:
        return 0
    
    result = float(history[0])
    current_operator = None

    for entry in history[1:]:
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
    print('List of available operations: +, -, *, /')
    print('Press "=" to get result or press "space" to exit')
    print('Press "d" to delete the last entry, "z" to reset the result to zero, or "h" to show history')

    history = []  # Initialize history

    # Ask for the first number
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
            history.append(first_input)  # Add the first number to history
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    clear_screen()

    while True:
        try:
            # Ask for operator
            operator = input("Enter an operator (+, -, *, /), 'd' to delete, 'z' to reset, 'h' to show history, or press 'space' to exit: ").strip()

            if operator == '':
                print('Exiting the calculator. Goodbye!')
                break

            # Show history
            if operator == 'h':
                if history:
                    print("Calculation History: " + " ".join(history))
                else:
                    print("History is empty.")
                continue

            # Handle reset
            if operator == 'z':
                history = []  # Clear history
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
                        history.append(first_input)  # Add the first number to history
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                clear_screen()
                continue

            # Handle delete last entry
            if operator == 'd':
                if history:
                    last_entry = history.pop()  # Remove last entry
                    print(f"Deleted last entry: {last_entry}")
                    if not history:
                        print("No entries left.")
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
                                history.append(first_input)  # Add the first number to history
                                break
                            except ValueError:
                                print("Invalid input. Please enter a valid number.")
                    clear_screen()
                else:
                    print("No entries to delete.")
                continue

            # Check if valid operator
            if operator in ['+', '-', '*', '/']:
                history.append(operator)
                clear_screen()

                # Now ask for the next number
                user_input = input("Enter the next number, 'h' to show history, or 'd' to delete: ").strip()
                if user_input == '':
                    print('Exiting the calculator. Goodbye!')
                    break

                if user_input == 'h':
                    if history:
                        print("Calculation History: " + " ".join(history))
                    else:
                        print("History is empty.")
                    continue

                elif user_input == 'd':
                    if history:
                        last_entry = history.pop()  # Remove last entry
                        print(f"Deleted last entry: {last_entry}")
                        if not history:
                            print("No entries left.")
                            continue
                    else:
                        print("No entries to delete.")
                    continue

                try:
                    num = float(user_input)
                    history.append(user_input)  # Add number to history
                    clear_screen()
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    history.pop()  # Remove invalid operator
                    continue

            elif operator == '=':
                if not history:
                    print("Nothing to calculate. Please enter numbers first.")
                    continue
                try:
                    result = calculate_result(history)
                    print(f"The result is: {result}")
                except ZeroDivisionError as e:
                    print(e)
                continue
            else:
                print("Invalid operator. Please try again.")

        except ValueError:
            print('Invalid input. Please enter numeric values.')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    calculator()
