import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    print('Welcome!')
    print('List of available operations: +, -, *, /')
    print('Press "=" to get result or press "space" to exit')
    print('Press "d" to delete the last entry or "z" to reset the result to zero')

    while True:
        try:
            # Initialize
            user_input = input("Enter the first number or press 'space' to exit: ").strip()
            if user_input == '':
                print('Exiting the calculator. Goodbye!')
                break

            result = float(user_input)
            history = [result]  # Store the history of entries
            clear_screen()

            while True:
                operators = ['+', '-', '*', '/', '=', 'd', 'z']
                # Select operator
                operator = input("Enter an operator (+, -, *, /), 'd' to delete the last entry, 'z' to reset, or press 'space' to exit: ").strip()

                if operator == '':
                    print('Exiting the calculator. Goodbye!')
                    return

                if operator not in operators:
                    print("Invalid operator. Please use one of +, -, *, /, '=' to see result, 'd' to delete, or 'z' to reset.")
                    continue

                # Handle delete last entry
                if operator == 'd':
                    if len(history) > 1:
                        last_entry = history.pop()  # Remove last entry
                        result = history[-1]  # Update result to the previous value
                        print(f"Deleted last entry: {last_entry}. Current result: {result}")
                    else:
                        print("No entries to delete.")
                    continue

                # Handle reset
                if operator == 'z':
                    result = 0  # Reset result
                    history = [result]  # Clear history
                    print("Result reset to zero. Please enter a new number to start over.")
                    user_input = input("Enter the first number or press 'space' to exit: ").strip()
                    if user_input == '':
                        print('Exiting the calculator. Goodbye!')
                        return
                    result = float(user_input)
                    history = [result]
                    clear_screen()
                    continue

                # Handle show result
                if operator == '=':
                    clear_screen()
                    print(f"The result is: {result}")
                    print("Choose an operator, or press 'space' to exit, or '=' to see the result.")
                    continue

                clear_screen()
                # Get the next number
                user_input = input("Enter the next number, 'd' to delete the last entry, or press 'space' to exit: ").strip()
                if user_input == '':
                    print('Exiting the calculator. Goodbye!')
                    break

                try:
                    num = float(user_input)
                    history.append(num)  # Add to history
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue

                clear_screen()

                # Perform operations
                if operator == '+':
                    result += num
                elif operator == '-':
                    result -= num
                elif operator == '*':
                    result *= num
                elif operator == '/':
                    if num == 0:
                        print("Division by zero is not allowed. Try again.")
                        history.pop()  # Remove invalid entry
                        continue
                    result /= num

                # Add the result to history
                history[-1] = result
                print("Choose an operator, or press 'space' to exit, or '=' to see the result.")

        except ValueError:
            print('Invalid input. Please enter numeric values.')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    calculator()
