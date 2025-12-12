# Check if string is a palindrome.
from time import time  # I tried to use time(), but calling time takes long time and the result of comparing is not true
import timeit

def check_polindrome(word:str)->bool:
    if word == word[::-1]:
        return True
    return False

def check_polindrome2(word:str)->bool:
    if "".join(reversed(word)) == word:
        return True
    return False



word="abba"*100

time1 = timeit.timeit(lambda: check_polindrome(word), number=1000)
time2 = timeit.timeit(lambda: check_polindrome2(word), number=1000)

print(f"word[::-1] method: {time1:.6f} секунд")
print(f"reversed() method:  {time2:.6f} секунд")
print(f"Разница: {abs(time1 - time2):.6f} секунд")
