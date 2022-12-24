from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def sub(n1, n2):
    return n1 - n2


# Multiply
def mult(n1, n2):
    return n1 * n2


# Divide
def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}


def calculator():
    print(logo)
    flag = True

    num1 = float(input("What's the first number?: "))

    for operation in operations:
        print(operation)

    while flag:
        operation_symbol = input("Pick an operation: ")
        calculation_function = operations[operation_symbol]

        num2 = float(input("What's the next number?: "))

        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} =  {answer}")

        if input(f"Type Y to continue calculation with {answer} or N to start new calculation") == "y":
            num1 = answer
        else:
            flag = False
            calculator()


calculator()
