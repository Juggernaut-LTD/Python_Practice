def calculate_inputs(value_1, value_2, math_operator):
    output_value = 0
    
    if math_operator == "+" or math_operator == "add":
        output_value = value_1 + value_2

    if math_operator == "-" or math_operator == "sub":
        output_value = value_1 - value_2

    if math_operator == "/" or math_operator == "div":
        output_value = value_1 / value_2

    if math_operator == "*" or math_operator == "mult":
        output_value = value_1 * value_2

    print("Your result is: " + str(output_value))

    return

value_1 = int(input("Please enter the first value: "))
value_2 = int(input("Please enter the second value: "))
math_operator = input("Please enter the operator in either text or symbol format (add, +, sub, -, div, /, mult, *): ")

calculate_inputs(value_1, value_2, math_operator)