from typing import List

def move_zeros_end(arr: List[int]):
    write = 0  # куда писать след. ненулевой элемент
    n = len(arr)

    for i in range(n):
        if arr[i] != 0:
            arr[write] = arr[i]
            write += 1

    # оставить нули в конце
    while write < n:
        arr[write] = 0
        write += 1

    return arr

# print(move_zeros_end([0,1,0,3,12]))
