#calculator.py has 4 functions: add, subtract, multiply, divide

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error: Cannot divide by zero"
    return a/b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+,-,*,/): ")
    num2 = float(input("Enter second number: "))

    if operator in operations:
        result = operations[operator](num1 , num2)
        print(f"\nResult: {result}")
    else:
        print("Invalid operator")
except ValueError:
    print("Invalid input! Please enter valid numbers.")
    