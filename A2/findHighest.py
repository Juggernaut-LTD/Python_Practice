def findHighest(input_array):
    high_num = 0

    for num in input_array:
        if num > high_num:
            high_num = num
    
    print(high_num)

    return

input_array = [-10, -5, -15, -3, 1, 6, 9]

findHighest(input_array)