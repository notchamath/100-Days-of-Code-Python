import os

def clear():
    os.system("clear")

# Add 
def add(n1, n2):
    return n1 + n2
    
# Subtract 
def sub(n1, n2):
    return n1 - n2

# Multiply 
def mul(n1, n2):
    return n1 * n2

# Divide 
def div(n1, n2):
    return n1 / n2

# Dictionary holds above functions using operation symbol as key
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():

    # Get first number from user
    num1 = float(input("What is the first number? "))

    is_calculating = True

    while is_calculating:

        # Print operation symbols
        for symbol in operations:
            print(symbol)

        # Get operation they want to perform from user
        operation = input("Pick an operation from the line above: ")

        # Get second number from user
        num2 = float(input("What is the next number? "))

        # Perform operation
        answer = operations[operation](num1, num2)

        # Print answer
        print(f"{num1} {operation} {num2} = {answer}")

        # Ask user if they like to continue with more calculations with the result
        restart = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        # if yes, restart loop with result as the first number. Else exit loop
        if restart == 'y':
            num1 = answer
        else:
            is_calculating = False
            clear()
            calculator()

calculator()