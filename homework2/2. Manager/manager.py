
#Implement a manager that suppresses passed errors, but logs them.
# all logs are writing into logs.txt




class ErrorLogger:
    def __init__(self, *error_types):
        self.errors_to_catch = error_types
        self.caught_errors = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            return True
            
        if not self.errors_to_catch or exc_type in self.errors_to_catch:
            error_info = f"{exc_type.__name__}: {exc_value}"
            self.caught_errors.append(error_info)
            
            with open("./logs.txt", "a") as f:
                f.write(f"ERROR: {error_info}\n")
            
            print(f"Caught error: {error_info}")
            return True
            
        return False
    
    def show_errors(self):
        return self.caught_errors

# Test it
logger = ErrorLogger(ValueError, ZeroDivisionError)

# This error will be caught and logged
with logger:
    raise ValueError("Something went wrong")

# This one too
with logger:
    raise ZeroDivisionError("Can't divide by zero")

# This error will NOT be caught
try:
    with logger:
        raise TypeError("Wrong type")
except:
    print("This error was not caught!")

print("\nAll caught errors:")
for err in logger.show_errors():
    print(f"- {err}")