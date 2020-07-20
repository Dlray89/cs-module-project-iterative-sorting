def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) -1

    while low <= high:
        middle = low + high // 2

        if target < arr[int(middle)]:
            high = int(middle) - 1
        elif target > arr[int(middle)]:
            low = int(middle) + 1
        else:
            return int(middle)


    # Your code here


    return -1  # not found
