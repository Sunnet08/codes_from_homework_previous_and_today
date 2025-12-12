from typing import List

def single_number(arr: List[int]):
    res = 0
    for x in arr:
        res ^= x  # XOR убирает пары
    return res

# print(single_number([4,1,2,1,2]))
