
# it is more interesting variant of transaction, second variant of how I could think and plan the logic of the program 

# Create a transactional object saver: 
# if there is not error – changed object is being returned, 
# but on error original object should be preserved.

# For example we have two bank accounts. We want from one account send some money to another account.
# If we have any issues while the transaction, we will not save changes and return back all changes

# transactions = [[id_of_first_account, id_of_second_account, amount_of_transaction]] we save all transactions to "transactions2.txt" file


import copy
import pathlib


# making banck accounts for sending money between accounts
class BankAccount:
    def __init__(self, name, user_id, account_balance=0):
        self.user_id = user_id
        self.name = name
        self.account_balance = account_balance
    
    def send_money(self, another_user, amount):
        if self.account_balance < amount:
            raise ValueError(f"Not enough amount of money in your bank balance. Your balance: {self.account_balance}, NEEDED: {amount}")
        if amount <= 0:
            raise ValueError("Amount of transactions have to be positive !")
        
        self.account_balance -= amount
        another_user.account_balance += amount
        return True
    
    def __repr__(self):
        return f"BankAccount({self.name}, id:{self.user_id}, balance:{self.account_balance})"

class TransactionalObjectSaver:
    def __init__(self, *objects):
        self.original_objects = objects
        self.original_states = []
        self.working_copies = []
    
    def __enter__(self):
        print("Started the transaction")
        
        for obj in self.original_objects:
            self.original_states.append(copy.deepcopy(obj))
            self.working_copies.append(obj)
        
        return self.working_copies
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Transaction is successfull!")
            self._save_transaction_to_file()
            return False
        else:
            print(f"ERROR of transaction: {exc_type.__name__}. returning the changes")
            self._rollback_changes()
            return False
    
    def _rollback_changes(self):
        for i, original_state in enumerate(self.original_states):
            self.original_objects[i].__dict__.update(original_state.__dict__)
    
    def _save_transaction_to_file(self):
        transaction_file = pathlib.Path("transactions2.txt")
        
        with open(transaction_file, "a", encoding="utf-8") as f:
            for i, obj in enumerate(self.original_objects):
                original_balance = self.original_states[i].account_balance
                current_balance = obj.account_balance
                
                if original_balance != current_balance:
                    change = current_balance - original_balance
                    direction = "ACCEPT" if change > 0 else "SEND"
                    f.write(f"{obj.name} (id:{obj.user_id}): {direction} {abs(change)} rub. "
                           f"[{original_balance} -> {current_balance}]\n")
            
            f.write("---\n")

def main():
    ivan = BankAccount("IVAN", "user_001", 1000)
    maria = BankAccount("MARY", "user_002", 500)
    petr = BankAccount("PETR", "user_003", 200)
    
    print("Before the transaction:")
    print(ivan)
    print(maria)
    print(petr)
    print()

# no any errors and our transaction will be done    
    try:
        with TransactionalObjectSaver(ivan, maria) as [ivan_temp, maria_temp]:
            ivan_temp.send_money(maria_temp, 300)
            print("Перевод выполнен внутри транзакции")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\nAfter successful transaction:")
    print(ivan)
    print(maria)
    print()

# here we check our code with the exception (With error)   
    try:
        with TransactionalObjectSaver(ivan, maria, petr) as accounts:
            accounts[0].send_money(accounts[1], 200)
            accounts[1].send_money(accounts[2], 100)
            print("Two transactions are done")
            raise ValueError("Error with our Bank!")
            
    except Exception as e:
        print(f"Поймана ошибка: {e}")
    
    print("\n After unsuccess transaction (должен быть откат):")
    print(ivan)
    print(maria)
    print(petr)

if __name__ == "__main__":
    main()