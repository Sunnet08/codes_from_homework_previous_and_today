# Create a prime number generator: generator should return all prime numbers 
# less than given n.



def generate_primes(n):
    if n <= 2:
        return
    yield 2
    for num in range(3, n, 2):
        is_prime = True
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num



# Test cases
def test_generate_primes():
    # Test n <= 2
    assert list(generate_primes(1)) == []
    assert list(generate_primes(2)) == []
    
    # Test small values
    assert list(generate_primes(3)) == [2]
    assert list(generate_primes(4)) == [2, 3]
    assert list(generate_primes(8)) == [2, 3, 5, 7]
    assert list(generate_primes(10)) == [2, 3, 5, 7]
    
    # Test medium values
    assert list(generate_primes(20)) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert list(generate_primes(30)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    # Test edge case
    assert list(generate_primes(100))[-1] == 97  # last prime < 100
    
    print("All tests passed!")



# Run tests
test_generate_primes()
