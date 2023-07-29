def findHighestVal(arr):
    if not arr:
        raise ValueError("Array is empty")

    maxElement = arr[0]
    for num in arr[1:]:
        if num > maxElement:
            maxElement = num
    return maxElement
