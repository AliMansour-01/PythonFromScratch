#calculator using functions with outputs

from calculator_art import logo

#Calculator

#ADD
def add(n1, n2):
    return n1 + n2

#Subtract
def sub(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
   return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for keys in operations:
        print(keys)

    should_continue = True

    while should_continue:
        operations_symbol = input("Pick an operation from the above: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operations_symbol]
        answer1 = calculation_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer1}")
        choice = input(f"Type 'y' to continue calculating with {answer1}, 'n' for new calculation, and 'q' to quit: ").lower()
        if choice == 'y':
            num1 = answer1
        elif choice == 'n':
            should_continue = False
            calculator()
        else:
            should_continue = False

calculator()