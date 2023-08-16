"""12.Generator for Multiplication Table

Write a generator function that yields the multiplication table for a given number up to n.
Input: 3, 5
Output: 3, 6, 9, 12, 15"""

def muplitplicTable(x,n):
    for i in range(1,n+1):
        yield x*i

for i in muplitplicTable(3,5):
    print(i)