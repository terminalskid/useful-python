import math  # imports math module (not required yet, but useful later)

# Ask the user which operation they want
print("Enter an operator: x, +, -, /")
operator = input().strip().lower()  # get input, remove spaces, make lowercase

# Check if the operator is valid
if operator not in ["x", "*", "+", "-", "/"]:
    print("invalid operator")  # tell user if operator is not allowed
else:
    # Ask for the first number
    num1 = float(input("Enter first number: "))

    # Ask for the second number
    num2 = float(input("Enter second number: "))

    # If the operator is multiplication
    if operator == "x" or operator == "*":
        result = num1 * num2  # multiply the numbers

    # If the operator is addition
    elif operator == "+":
        result = num1 + num2  # add the numbers

    # If the operator is subtraction
    elif operator == "-":
        result = num1 - num2  # subtract the numbers

    # If the operator is division
    elif operator == "/":
        # Prevent division by zero
        if num2 == 0:
            print("Error: cannot divide by zero")
            exit()
        result = num1 / num2  # divide the numbers

    # Print the final answer
    print("Result:", result)
#done
