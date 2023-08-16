"""15.Generator for Geometric Progression

Write a generator function that yields a geometric progression with a given start, ratio, and length.
Input: 2, 3, 4
Output: 2, 6, 18, 54"""

def geoProg(start, ratio, length):
    yield start
    for i in range(1,length):
        start *= ratio
        yield start

for i in geoProg(2,3,4):
    print(i)