"""9.Generator to Yield Powers of Two

Write a generator function that yields the powers of two up to n.
Input: 4
Output: 1, 2, 4, 8"""

def powerGen(x):
    for i in range(0,x):
        yield 2**i

for i in powerGen(4):
    print(i)