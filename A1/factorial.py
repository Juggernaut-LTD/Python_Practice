def calculate_factorial(num_input):
    total_factorial = 1

    for num in range(1, num_input +1):
        total_factorial *= num

    print("The value of " + str(num_input) + " factorial is: " + str(total_factorial))

    return

num_input = int(input("Enter a number to calculate its factorial: "))

calculate_factorial(num_input)