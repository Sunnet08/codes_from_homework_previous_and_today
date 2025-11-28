# Implement function to generate combinations of length k 
# from sequence: generate_combinations(sequence, k)


def generate_combinations(sequence, k):
    if k == 0:
        yield ()
        return
    if len(sequence) == 0 or k > len(sequence):
        return
    for i in range(len(sequence)):
        current = sequence[i]
        remaining = sequence[i + 1:]
        for combo in generate_combinations(remaining, k - 1):
            yield (current,) + combo



def test_generate_combinations():
    # Test 1: basic case
    assert list(generate_combinations([1, 2, 3], 2)) == [(1, 2), (1, 3), (2, 3)]
    # Test 2: k = 1
    assert list(generate_combinations([1, 2, 3], 1)) == [(1,), (2,), (3,)]
    # Test 3: k equals length
    assert list(generate_combinations([1, 2, 3], 3)) == [(1, 2, 3)]
    # Test 4: k > length
    assert list(generate_combinations([1, 2], 3)) == []
    # Test 5: empty sequence
    assert list(generate_combinations([], 1)) == []
    # Test 6: k = 0
    assert list(generate_combinations([1, 2, 3], 0)) == [()]
    # Test 7: single element
    assert list(generate_combinations([42], 1)) == [(42,)]
    assert list(generate_combinations([42], 2)) == []
    # Test 8: two elements, k=2
    assert list(generate_combinations([10, 20], 2)) == [(10, 20)]
    print("All tests passed!")

test_generate_combinations()
