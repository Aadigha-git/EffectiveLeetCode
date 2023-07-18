def longestPalindrome(s):
    # Create a frequency dictionary for the letters in the string
    freq = {}

    # Count the occurrences of each letter
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    length = 0
    odd_count = 0

    # Iterate through the frequency dictionary
    for count in freq.values():
        # If the count is even, add it to the length
        if count % 2 == 0:
            length += count
        # If the count is odd, add the count - 1 to the length
        # and set odd_count to 1 (indicating an odd count has been encountered)
        else:
            length += count - 1
            odd_count = 1

    # If there was at least one letter with an odd count, add 1 to the length
    if odd_count:
        length += 1

    return length

s = "abccccdd"
longest_palindrome_length = longestPalindrome(s)
print(longest_palindrome_length)

"""
Question17:

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""