"""14.Nested Functions for String Manipulation

Write a function containing nested functions to perform various string manipulations like uppercase, lowercase, and capitalization.
Input: "hello", "uppercase"
Output: "HELLO"""

def TypeOp(txt,operation):
    def Uppercase(txt):
        return txt.upper()
    def Lowercase(txt):
        return txt.lower()
    def Capitalize(txt):
        return txt.capitalize()
    if operation == "Uppercase":
        return Uppercase(txt)
    elif operation == "Lowercase":
        return Lowercase(txt)
    elif operation == "Capitalize":
        return Capitalize(txt)

print(TypeOp("pisanie","Uppercase"))
print(TypeOp("pisanie","Lowercase"))
print(TypeOp("pisanie","Capitalize"))