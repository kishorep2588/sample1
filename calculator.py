

while True:
    num1 = input("Enter the first number (or 'q' to quit): ")
    num2 = input("Enter the second number (or 'q' to quit): ")
    operation = input("Enter the operation (+, -, *, /) (or 'q' to quit): ")

    if num1.lower() == 'q' or num2.lower() == 'q' or operation.lower() == 'q':
        print("Exiting the calculator. Goodbye!")
        break
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = num1 / num2
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")
        continue
    print(f"The result of {num1} {operation} {num2} is: {result}")
    