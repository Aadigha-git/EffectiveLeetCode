def canConstruct(ransomNote, magazine):
    # Create frequency dictionaries for both strings
    ransom_freq = {}
    magazine_freq = {}

    # Count the occurrences of each character in ransomNote
    for char in ransomNote:
        if char in ransom_freq:
            ransom_freq[char] += 1
        else:
            ransom_freq[char] = 1

    # Count the occurrences of each character in magazine
    for char in magazine:
        if char in magazine_freq:
            magazine_freq[char] += 1
        else:
            magazine_freq[char] = 1

    # Check if the ransomNote can be constructed using the letters from magazine
    for char, count in ransom_freq.items():
        if char not in magazine_freq or count > magazine_freq[char]:
            return False

    return True
ransomNote = "aa"
magazine = "ab"

result = canConstruct(ransomNote, magazine)
print(result)  # Output: True
