"""7.Nested Functions for Arithmetic Operations

Write a function containing nested functions for addition, subtraction, multiplication, and division. The outer function should take two numbers and an operator as input and return the result.
Input: 10, 5, "add"
Output: 15"""

def Math(a,b,operation):
    def Add(a,b):
        return a+b
    def Substract(a,b):
        return a-b
    def Multiply(a,b):
        return a*b
    def Divide(a,b):
        return a/b
    if operation == "Add":
        return(Add(a,b))
    elif operation == "Substract":
        return(Substract(a,b))
    elif operation == "Multiply":
        return(Multiply(a,b))
    elif operation == "Divide":
        return(Divide(a,b))

print(Math(3,2,"Divide"))