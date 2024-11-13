# Get input from the user
inputNum1 = float(input("Enter the first number: "))
inputNum2 = float(input("Enter the second number: "))
numOperation = input("Choose an operation (+, -, *, /): ")

# Perform the calculation based on the chosen operation
if numOperation == "+":
    calculatedResult = inputNum1 + inputNum2
    print(f"{inputNum1} + {inputNum2} = {calculatedResult}")
elif numOperation == "-":
    calculatedResult = inputNum1 - inputNum2
    print(f"{inputNum1} - {inputNum2} = {calculatedResult}")
elif numOperation == "*":
    calculatedResult = inputNum1 * inputNum2
    print(f"{inputNum1} * {inputNum2} = {calculatedResult}")
elif numOperation == "/":
    # Check for division by zero
    if inputNum2 != 0:
        calculatedResult = inputNum1 / inputNum2
        print(f"{inputNum1} / {inputNum2} = {calculatedResult}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose from +, -, *, or /.")
