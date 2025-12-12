from typing import List

def bubble_sort(arr: List[int]):
    n = len(arr)

    for i in range(n):
        swapped = False  # был ли обмен
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  # если нет обменов — отсортировано
            break

    return arr

# print(bubble_sort([5,2,8,1,3]))
