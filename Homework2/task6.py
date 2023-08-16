"""6.Generator for Prime Numbers

Write a generator function that yields prime numbers up to n.
Input: 10
Output: 2, 3, 5, 7"""

def isPrime(x):
    if x<=1:
        return False
    else:
        for i in range(2,x):
            if x%i == 0:
                return False
        return True

def primeGen(x):
    for i in range(2,x+1):
        if isPrime(i):
            yield i

for i in primeGen(10):
    print(i)