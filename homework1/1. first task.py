# Create an iterator to chain multiple sequences: chain_sequences(*sequences)



class chain_sequences:
    def __init__(self, *sequences):
        self.sequences = sequences
        self.seq_index = 0  
        self.item_index = 0 
    def __iter__(self):
        return self
    def __next__(self):
        while self.seq_index < len(self.sequences):
            current_seq = self.sequences[self.seq_index]
            if self.item_index < len(current_seq):
                item = current_seq[self.item_index]
                self.item_index += 1
                return item
            else:
                self.seq_index += 1
                self.item_index = 0  
        raise StopIteration


# " Example usage:"
if __name__ == "__main__":
    chained = chain_sequences([1, 2, 3], [4], [5])
    for item in chained:
        print(item)