"""
16.Function to Compute Power of Variable Arguments
Write a function that takes a variable number of arguments and returns the result of raising the first argument to the power of the rest in order.
Input: 2, 3, 2
Output: 64 (i.e., 2^3^2 = 64)"""

def naStepen(*args):
    result = args[0]
    i = 0
    for arg in args:
        if i > 0:
            result **= arg
        i += 1
    return result

print(naStepen(2,3,2))