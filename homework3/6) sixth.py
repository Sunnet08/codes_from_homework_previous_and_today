from typing import List

def three_sum(arr: List[int], target: int):
    n = len(arr)
    if n < 3:
        return -1

    for i in range(n - 2):
        left = i + 1
        right = -1  

        # следим чтобы left не пересёкся с right
        while left < (n + right):
            s = arr[i] + arr[left] + arr[right]
            if s == target:
                return (arr[i], arr[left], arr[right])
            elif s < target:
                left += 1
            else:
                right -= 1

    return -1

# print(three_sum([1,2,3,4,5,6], 10))
