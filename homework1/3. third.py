# Create a prime number generator: generator should return all prime numbers 
# less than given n.



def generate_primes(n):
    if n <= 2:
        # выходим из функции не делая ничего так как нам нужно число больше чем 2
        return
    # начинаем с 2
    yield 2
    # берем интервал от 3 до n с шагом 2, так как все четные числа больше чем 2 делятся на 2, нам нужны только те которые деляться на себя и на 1
    for num in range(3, n, 2):
        is_prime = True
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num


print(list(generate_primes(2)))
