def calculator():

  print('Welcome!')
  print('List of available of operations: +, -, *, /')
  print('Press "=" to get result or press "esc" to exit')


  while True: 
    try: 
      # Initialize 
      user_input = input("Enter the number or press 'space' to exit: ").strip()
      if user_input == '': 
        print('Exiting the calculator. Goodbye!')
        break

      result = float(user_input)

      while True: 
        operators = ['+', '-', '*', '/', '=']
        # Select operator
        operator = input("Enter an operator  (+, -, *, /) or press '=' to get result or press 'space' to exit: ").strip()

        if operator == '':
          print('Exiting the calculator. Goodbye!')
          return
        
        if operator not in operators:
          print("Invalid operator. Please use one of +, -, *, / or press '=' to get result")
        
        if operator == '=': 
          print(f"The result is: {result}")
          continue
        
        
        # get the next number 
        user_input = input("Enter the numebr or press 'space' to exit: ").strip()
        if user_input == '': 
          print('Exiting the calculator. Goodbye!')
          break

        num = float(user_input)
        

        # perform operations 
        if operator == '+': 
          result += num
        elif operator == '-': 
          result -= num  
        elif operator == '*': 
          result *= num
        elif operator == '/': 
          if num == 0: 
            print('Error: Division by zero is not allowed')
            continue
          result /= num 

    except ValueError:
      print('Invalid input. Please enter numeric values')
    except Exception as e: 
      print(f'An unexpected error occurred: {e}')

if __name__ == '__main__': 
  calculator()
      



