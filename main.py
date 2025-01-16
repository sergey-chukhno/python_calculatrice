import os
from history import * 

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Calculation funct
def calculate_expression(expression):
    # Func to apply operator
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

    # Func to establish priority
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    # Algorithm to traverse and parse expression
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

# Func to manage calculator functions (interface)
def calculator():

  while True:
      clear_screen()

      print("\nCurrent Entry: " + get_current_entry())

      user_input = input("\nEnter a number/operator ('+', '-', '*', '/', '(', ')', '='), \n'd' to delete last entry, 'c' to clear entry and history, 'h' to show history, \n's' to save history file, 'o' to open history file, 'r' to remove history file, or 'space' to exit: ").strip()

      if user_input == '':  # Exit
          print("Exiting the calculator. Goodbye!")
          break

      if user_input == 'h':  # Show history
          print("\nCurrent Entry: " + get_current_entry())
          print("\nHistory: " + " | ".join(get_history()) if get_history() else "History is empty.")
          input("\nPress Enter to return to the main prompt...")
          continue
      
      if user_input == 'o':  # Open a file
          file_to_open = input("\nEnter the name of the file you want to open (e.g., 'history.json'): ").strip()
          open_json_file(file_to_open)
          input("\nPress Enter to return to the main prompt...")
          continue


      if user_input == 's':  # Save history to a file
          new_filename = input("\nEnter the new file name (e.g., 'new_history.json'): ").strip()
          if new_filename:
              with open(new_filename, 'w') as file:
                  json.dump(history, file)
              print(f"History saved to {new_filename}")
          else:
              print("Invalid name. History not saved.")
          input("\nPress Enter to return to the main prompt...")
          continue
      
      if user_input == 'r':  # Remove a file
        file_to_remove = input("\nEnter the name of the file you want to delete (e.g., 'history.json'): ").strip()
        if os.path.exists(file_to_remove):
            os.remove(file_to_remove)
            print(f"File '{file_to_remove}' has been deleted.")
        else:
            print(f"Error: File '{file_to_remove}' does not exist.")
        input("\nPress Enter to return to the main prompt...")
        continue


      if user_input == 'd':  # Delete the last entry in current calculation
          delete_last_from_current_entry()
          continue

      if user_input == 'c':  # Clear entry and history
          reset_history()
          print("Reset complete. Start a new calculation.")
          continue

      if user_input in ['+', '-', '*', '/', '(', ')']: # Handling operators
          if user_input == '(':
              if not get_current_entry() or get_current_entry()[-1] in ['+', '-', '*', '/', '(']:
                  add_to_current_entry(user_input)
              else:
                  print("Invalid input. '(' must follow an operator or be at the start.")
          elif user_input == ')':
              current_entry = get_current_entry()
              if current_entry.count('(') > current_entry.count(')'):
                  add_to_current_entry(user_input)
              else:
                  print("Invalid input. Ensure proper use of '('.")
          else:
              if not get_current_entry():
                  print("Enter a number first.")
                  continue
              add_to_current_entry(user_input)
          continue

      if user_input == '=':  # Finalize current calculation
          current_entry = get_current_entry()
          if not current_entry or current_entry[-1] in ['+', '-', '*', '/', '(']:
              print("Complete the expression before pressing '='.")
              continue
          try:
              result = calculate_expression(current_entry)
              print(f"Result: {result}")
              finalize_current_entry(result)
          except ZeroDivisionError as e:
              print(f"Error: {e}")
              reset_history()
              input("\nPress Enter to return to the main prompt...")
              continue
          except Exception as e:
              print(f"Error: {e}")
          continue

      try:
          float(user_input)
          add_to_current_entry(user_input)
      except ValueError:
          print("Invalid input. Please enter a number or operator.")
          input("\nPress Enter to return to the main prompt...")
          continue

if __name__ == "__main__":
    calculator()







