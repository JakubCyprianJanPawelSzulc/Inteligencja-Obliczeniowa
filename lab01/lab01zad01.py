def prime(n):
    if n < 2:  # Liczby mniejsze niż 2 nie są uważane za liczby pierwsze
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(prime(2))
print(prime(3))
print(prime(4))
print(prime(21))

def select_primes(array):
    return [x for x in array if prime(x)]

print(select_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))