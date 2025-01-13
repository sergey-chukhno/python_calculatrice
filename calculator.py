def calculator():

  print('Welcome!')
  print('List of available of operations: +, -, *, /')
  print('Press "=" to get result or press "esc" to exit')


  while True: 
    try: 
      # Initialize result
      result = float(input('Enter number:').strip())

      while True: 
        operators = ['+', '-', '*', '/']
        # Select operator
        operator = input("Enter an operator  (+, -, *, /) or press '=' to get result").strip()
        if operator == '=': 
          print(f"The result is: {result}")
        if operator not in operators:
          print("Invalid operator. Please use one of +, -, *, / or press '=' to get result")
        
        # get the next number 
        num = float(input("Enter number:").strip())

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
          result  /= num 

    except ValueError:
      print('Invalid input. Please enter numeric values')
    except Exception as e: 
      print(f'An unexpected error occurred: {e}')

if __name__ == '__main__': 
  calculator()
      



