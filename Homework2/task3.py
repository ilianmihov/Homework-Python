"""3.Nested Function for Calculating Factorial

Write a function that contains a nested function to calculate the factorial of a number.
Input: 5
Output: 120"""

def factoriel(x):
    def control(x):
        start = 1
        for i in range(1,x+1):
            start *= i
        return start
    return control(x)

print(factoriel(5))