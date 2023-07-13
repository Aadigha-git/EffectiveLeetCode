# this is the brute force approach to solve the problem statement
def twosum(nums, target):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]
            
nums = [2,1,5,3]
target = int(input("Enter the number you want to search for: "))

print(twosum(nums, target))


"""
Question1 : TwoSum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""