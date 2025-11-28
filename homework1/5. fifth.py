# Implement multi-dimensional array iterator (without additional list creation)



def flatten_iterate(arr):
    for item in arr:
        if isinstance(item, list):
            yield from flatten_iterate(item)
        else:
            yield item



nums = [4, [5], 3, [2]]

print(list(flatten_iterate(nums)))