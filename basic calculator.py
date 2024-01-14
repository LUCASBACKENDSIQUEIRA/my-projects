def calculator():
    # Take user input for numbers and operator
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

# Perform calculations based on the operator
    
    if operator == '+':
      result = num1 + num2
    elif operator == '-':
      result = num1 - num2
    elif operator == '*':
      result = num1 * num2
    elif operator == '/':
      # Check for division by zero
       if num2 == 0:
           print("Error: Cannot divide by zero.")
           return
       result = num1 / num2
    else:
       print("Invalid operator. Please enter +, -, *, or /.")
       return
    
    # Print the result
    print("Result: {:.2f}".format(result))

#Call the calculator function
calculator()
