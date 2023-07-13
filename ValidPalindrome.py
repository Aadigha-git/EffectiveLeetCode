def PalindromeCheck(s):
    
    s = s.lower()  
    s = "".join(char for char in s if char.isalnum())
    return s == s[::-1]

string = "race  car"

print(PalindromeCheck(string))

"""
Question5:
A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""