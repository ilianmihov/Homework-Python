"""2.Generator to Yield Fibonacci Sequence

Write a generator function that yields the Fibonacci sequence up to n numbers.
Input: 5
Output: 0, 1, 1, 2, 3"""

def Fibonacci(x):
    a = 0
    b = 1
    for i in range(x):
        yield a
        temp = a
        a += b
        b = temp


for i in Fibonacci(5):
    print(i)