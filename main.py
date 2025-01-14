import os
import history

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_expression(expression):
    """Evaluate a mathematical expression with parentheses and operator precedence."""
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            values.append(left / right)

    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    operators = []
    values = []
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        if expression[i] == '(':
            operators.append(expression[i])
        elif expression[i].isdigit() or (expression[i] == '.' and i + 1 < len(expression) and expression[i + 1].isdigit()):
            num = []
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num.append(expression[i])
                i += 1
            values.append(float("".join(num)))
            i -= 1
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()  # Pop the '('
        elif expression[i] in ('+', '-', '*', '/'):
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(expression[i])):
                apply_operator(operators, values)
            operators.append(expression[i])
        else:
            raise ValueError(f"Invalid character in expression: {expression[i]}")
        i += 1

    while operators:
        apply_operator(operators, values)

    return values[0]

def calculator():
    """Main calculator function."""
    print('Welcome!')
    print('List of available operations: +, -, *, /, (, ), =')
    print('Press "space" to exit')
    print('Press "d" to delete the last entry, "z" to reset, or "h" to show history')

    while True:
        # Display the current calculation and history
        clear_screen()

        # Display the current calculation
        print("\nCurrent Entry: " + history.get_current_entry())

        # Get user input
        user_input = input("\nEnter a number/operator ('+', '-', '*', '/', '(', ')', '='), 'd' to delete, 'z' to reset, 'h' for history, or 'space' to exit: ").strip()

        if user_input == '':  # Exit
            print("Exiting the calculator. Goodbye!")
            break

        if user_input == 'h':  # Show history
            print("\nCurrent Entry: " + history.get_current_entry())
            print("\nHistory: " + " | ".join(history.get_history()) if history.get_history() else "History is empty.")
            input("\nPress Enter to return to the main prompt...")  # Wait for user to press Enter to return
            continue

        if user_input == 'd':  # Delete last entry in current calculation
            history.delete_last_from_current_entry()
            continue

        if user_input == 'z':  # Reset the calculator
            history.reset_history()
            print("Reset complete. Start a new calculation.")
            continue

        if user_input in ['+', '-', '*', '/', '(', ')']:  # Add operator or parentheses to the current entry
            if user_input == '(':
                # Allow starting an expression with '('
                if not history.get_current_entry() or history.get_current_entry()[-1] in ['+', '-', '*', '/', '(']:
                    history.add_to_current_entry(user_input)
                else:
                    print("Invalid input. '(' must follow an operator or be at the start.")
            elif user_input == ')':
                # Ensure '(' exists and '(' count > ')' count
                current_entry = history.get_current_entry()
                if current_entry.count('(') > current_entry.count(')'):
                    history.add_to_current_entry(user_input)
                else:
                    print("Invalid input. Ensure proper use of '('.")
            else:
                # Add standard operators
                if not history.get_current_entry():  # Avoid starting with an operator
                    print("Enter a number first.")
                    continue
                history.add_to_current_entry(user_input)
            continue

        if user_input == '=':  # Finalize current calculation
            current_entry = history.get_current_entry()
            if not current_entry or current_entry[-1] in ['+', '-', '*', '/', '(']:  # Avoid incomplete expressions
                print("Complete the expression before pressing '='.")
                continue
            try:
                result = calculate_expression(current_entry)
                print(f"Result: {result}")
                history.finalize_current_entry(result)
            except ZeroDivisionError as e:
                print(f"Error: {e}")
                history.reset_history()  # Reset the current entry completely, like pressing 'z'
                input("\nPress Enter to return to the main prompt...")  # Wait for user to press Enter to continue
                continue
            except Exception as e:
                print(f"Error: {e}")
            continue

        try:  # Add number to the current entry
            float(user_input)  # Validate it's a number
            history.add_to_current_entry(user_input)
        except ValueError:
            # Display error message and wait for user input to continue
            print("Invalid input. Please enter a number or operator.")
            input("\nPress Enter to return to the main prompt...")  # Wait for user to press Enter to return
            continue

if __name__ == "__main__":
    calculator()




