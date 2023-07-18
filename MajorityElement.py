def majorityElement(nums):
    freq = {}
    for char in nums:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    n = len(nums)
    majority_count = n // 2

    for num, count in freq.items():
        if count > majority_count:
            return num

nums = [2, 2, 1, 1, 1, 2, 2]
majority = majorityElement(nums)
print(majority) 

"""
Question19:

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""