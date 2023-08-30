def containsDuplicate(nums):
    unique_elements = set()

    for num in nums:
        if num in unique_elements:
            return True
        unique_elements.add(num)

    return False
nums = [1, 2, 3, 4, 5]
result = containsDuplicate(nums)
print(result)

nums = [1, 2, 3, 2, 4, 5]
result = containsDuplicate(nums)
print(result)
