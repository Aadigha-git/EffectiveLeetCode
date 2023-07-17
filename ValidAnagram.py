def validAnagram(s,t):
    if len(s) != len(t):
        return False
    
    char_freq = {}
    # Count the frequencies of characters in s
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Compare the frequencies of characters in t with those in s
    for char in t:
        if char in char_freq:
            char_freq[char] -= 1
            if char_freq[char] == 0:
                del char_freq[char]
        else:
            return False

    # If all characters in t are accounted for, it is an anagram of s
    return len(char_freq) == 0

s = input("Enter the string to check the anagram validity " )
t = input("Enter what you want to check if it is an anagram ")
print(validAnagram(s, t))

"""
Question7:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""