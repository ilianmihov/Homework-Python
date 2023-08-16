"""5.Palindrome Checker Using Lambda

Write a lambda function that checks whether a given string is a palindrome.
Input: "madam"
Output: True"""

def isPalindrome(string):
    revStr = ""
    for c in string[::-1]:
        revStr += c
    if string.lower() == revStr.lower():
        return True
    return False

string = input()
print(isPalindrome(string))