import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    print('Welcome!')
    print('List of available operations: +, -, *, /')
    print('Press "=" to get result or press "space" to exit')

    while True:
        try:
            # Initialize
            user_input = input("Enter the first number or press 'space' to exit: ").strip()
            if user_input == '':
                print('Exiting the calculator. Goodbye!')
                break

            result = float(user_input)
            clear_screen()

            while True:
                operators = ['+', '-', '*', '/', '=']
                # Select operator
                operator = input("Enter an operator (+, -, *, /) or press 'space' to exit: ").strip()

                if operator == '':
                    print('Exiting the calculator. Goodbye!')
                    return

                if operator not in operators:
                    print("Invalid operator. Please use one of +, -, *, / or press '=' to get result.")
                    continue

                if operator == '=':
                    clear_screen()
                    print(f"The result is: {result}")
                    print("Choose an operator, or press 'space' to exit, or '=' to see the result.")
                    continue

                clear_screen()
                # Get the next number
                user_input = input("Enter the next number or press 'space' to exit: ").strip()
                if user_input == '':
                    print('Exiting the calculator. Goodbye!')
                    break

                num = float(user_input)
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
                      break
                      continue
                    result /= num

                print("Choose an operator, or press 'space' to exit, or '=' to see the result.")

        except ValueError:
            print('Invalid input. Please enter numeric values.')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    calculator()
