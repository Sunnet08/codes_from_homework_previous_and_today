# Implement function to generate combinations of length k 
# from sequence: generate_combinations(sequence, k)
# func([1, 2, 3], 2) -> (1, 2), (1, 3), (2, 3)


def generate_combinations(sequence, k):
    if k == 0:
        #возвращаем пустой кортеж
        yield ()
        # завершаем рекурсию так как не имеет смысла дальше продолжать
        return
    if len(sequence) == 0 or k > len(sequence):
        return
    for i in range(len(sequence)):
        current = sequence[i]
        remaining = sequence[i + 1:]
        for combo in generate_combinations(remaining, k - 1):
            yield (current,) + combo



