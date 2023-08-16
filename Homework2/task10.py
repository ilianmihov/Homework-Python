"""
10.Lambda Function to Filter Even Numbers

Write a lambda function that filters even numbers from a given list.
Input: [1, 2, 3, 4, 5]
Output: [2, 4]"""

def listFilter(lst):
    for i in lst:
        if i%2 != 0:
            lst.remove(i)

lst1 = [1,2,3,4,5]
listFilter(lst1)
print(lst1)