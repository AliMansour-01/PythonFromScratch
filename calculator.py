#calculator using functions with outputs



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

operators = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))

for keys in operators:
    print(keys)
operations_symbol = input("Pick an operation from the above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operators[operations_symbol]
answer = calculation_function(num1, num2)


print(f"{num1} {operations_symbol} {num2} = {answer}")




