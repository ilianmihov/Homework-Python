"""8.Lambda Function to Sort a List of Tuples

Write a lambda function that takes a list of tuples and sorts them by the second element.
Input: [(1, 2), (3, 1), (5, 0)]
Output: [(5, 0), (3, 1), (1, 2)]"""

def sortListOfTuples(lst):
    lst.sort(key = lambda x: x[1])
    return lst

print(sortListOfTuples([(1, 2), (3, 1), (5, 0)]))