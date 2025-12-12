# Create an iterator to chain multiple sequences: chain_sequences(*sequences)

class chain_sequences:
    def __init__(self, *sequences):
        self.sequences = sequences
        self.seq_index = 0  
        self.item_index = 0 
    def __iter__(self):
        return self
    def __next__(self):
        # берем каждый элемент в листе, до последнего элемента невключительно
        while self.seq_index < len(self.sequences):
            current_seq = self.sequences[self.seq_index]
            # берем элементы внутри каждого листа до последнего невключительно
            if self.item_index < len(current_seq):
                item = current_seq[self.item_index]
                self.item_index += 1
                return item
            # когда доходим до последнего элемента то меняем индекс sequence списков, и меняем индекс элемента внутри списка
            else:
                self.seq_index += 1
                self.item_index = 0  
        raise StopIteration


if __name__ == "__main__":
    chained = chain_sequences([1, 2, 3], [4], [5])
    for item in chained:
        print(item)