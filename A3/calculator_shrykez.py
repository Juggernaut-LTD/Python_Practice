import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)

def power(x, y):
    return x ** y

def scientific_calculator():
    print("Scientific Calculator")
    print("Operations: +, -, *, /, sqrt, ^")
    while True:
        operation = input("Enter an operation or 'q' to quit: ")
        if operation == 'q':
            break

        if operation not in ('+', '-', '*', '/', 'sqrt', '^'):
            print("Invalid operation. Please try again.")
            continue

        if operation in ('+', '-', '*', '/'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            else:
                try:
                    result = divide(num1, num2)
                except ValueError as e:
                    print(e)
                    continue

        elif operation == 'sqrt':
            num = float(input("Enter the number: "))
            try:
                result = square_root(num)
            except ValueError as e:
                print(e)
                continue

        elif operation == '^':
            num1 = float(input("Enter the base number: "))
            num2 = float(input("Enter the exponent: "))
            result = power(num1, num2)

        print("Result: ", result)

if __name__ == "__main__":
    scientific_calculator()
