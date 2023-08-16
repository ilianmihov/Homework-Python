"""4.Lambda Function Inside a Function

Write a function that takes a number n and returns a lambda function that multiplies its input by n.
Input: 3
Output: A function that multiplies its input by 3"""

i = int(input())
def func(i,n):
    x = lambda a,n : a*n
    print("A function that multiplies its input by ",n)
    return x(i,n)

print(func(i,3))