# Implement multi-dimensional array iterator (without additional list creation)
# flatten_iterate([1, 2, [3, [4], 5]]) -> 1, 2, 3, 4, 5


def flatten_iterate(arr):
    for item in arr:
        if isinstance(item, list):
            # yield from передает все yield из рекурсивного вызова "наверх"
            yield from flatten_iterate(item)
        else:
            yield item



nums = [4, [5], 3, [2]]

print(list(flatten_iterate(nums)))