# Create an iterator to zip multiple sequences: zip_sequences(*sequences)


class zip_sequences:
    def __init__(self, *sequences):
        self.sequences = sequences
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        for seq in self.sequences:
            if self.index >= len(seq):
                raise StopIteration
        result = []
        for seq in self.sequences:
            result.append(seq[self.index])
        self.index += 1
        return result


zipped = zip_sequences([1, 2, 3], ['a', 'b'], [10, 20, 30, 40])
for item in zipped:
    print(item)