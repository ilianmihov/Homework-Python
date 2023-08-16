"""
13.Lambda Function to Apply Function to List

Write a lambda function that takes another function and a list and applies the function to every element of the list.
Input: lambda x: x*2, [1, 2, 3]
Output: [2, 4, 6]"""
def strangeFunc(lambd,lst):
        return [lambd(x) for x in lst]

x = lambda a : a*2

print(strangeFunc(x,[1,2,3]))
