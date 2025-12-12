# Find two numbers in sorted array that are summing up to a
# given target or return -1.
from typing import List


# Idea: to have two vectors, one from beginning, another from the end
# if the sum of two numbers greater then target move second vector to left side,
# if the sum of two numbers are smaller than our target then move first vector to right side

# [1, 2, 3, 4, 5, 6]
# left = 0
# right = -1
# abs(right) + abs(left) > len(my_list) : return -1

def find_pair(arr:List[int], target:int):
    if len(arr) < 2 :
        return ("Not correct array")
    left_index = 0
    right_index = -1
    while (arr[left_index] + arr[right_index]) != target:
        if (arr[left_index] + arr[right_index]) > target:
            right_index -= 1
        elif (arr[left_index] + arr[right_index]) < target:
            left_index += 1
        if (abs(left_index) + abs(right_index)) > len(arr):
            return (-1)
    return (arr[left_index], arr[right_index])

    
print(find_pair([1, 10, 20, 30, 40], 45))

