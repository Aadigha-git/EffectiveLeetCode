# seems to be optimised
# use of array for this problem gave better result than the use of a stack
def validParanthesis(s):
    arr = []
    for char in s:
        if char in ['[', '{', '(']:
            arr.append(char)
        else:
            if arr and (  (arr[-1] == '(' and char == ')') or
                            (arr[-1] == '{' and char == '}') or 
                            (arr[-1] == '[' and char == ']')
                        ):
                arr.pop()
            else:
                return False
    return not arr
s = input("Enter the string to check the paranthesis of the strings. \n Accepted [],{},()\t" )
print(validParanthesis(s))

"""
Question2: Valid Paranthesis

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""