"""17.Function to Sort Variable Number of Lists
Write a function that takes a variable number of lists and returns a single list containing all the elements, sorted.
Input: [3, 1], [5, 2], [4, 0]
Output: [0, 1, 2, 3, 4, 5]"""

def listNumExctractSort(*args):
    lst = []
    for arg in args:
        for num in arg:
            lst.append(num)
    lst.sort()
    return lst

print(listNumExctractSort([3, 1], [5, 2], [4, 0]))