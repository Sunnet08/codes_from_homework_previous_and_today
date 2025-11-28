# Create a transactional object saver: 
# if there is not error – changed object is being returned, 
# but on error original object should be preserved.

import copy

class TransactionalListSaver:
    def __init__(self, original_list):
        self.original_list = original_list
        self.backup_list = None
    
    def __enter__(self):
        print("Starting transaction...")
        self.backup_list = copy.deepcopy(self.original_list)
        return self.original_list
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Transaction successful! Changes saved.")
            self._save_to_file()
        else:
            print("Transaction failed! Rolling back changes...")
            self._restore_backup()
        return False
    
    def _restore_backup(self):
        self.original_list.clear()
        self.original_list.extend(self.backup_list)
    
    def _save_to_file(self):
        with open("transactions.txt", "a") as f:
            f.write(f"Changed list: {self.original_list}\n")
            f.write("---\n")

# Testing щгк code
my_list = [1, 2, 3]

print("Before:", my_list)

# Successful transaction
with TransactionalListSaver(my_list) as temp_list:
    temp_list.append(4)
    temp_list.append(5)

print("After success:", my_list)

# Failed transaction
try:
    with TransactionalListSaver(my_list) as temp_list:
        temp_list.append(6)
        temp_list.append(7)
        raise ValueError("Test error!")
except:
    pass

print("After failure:", my_list)