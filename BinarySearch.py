def binary_search(lst, target):
    lb = 0                  # lower bound
    ub = len(lst) - 1       # upper bound

    while lb <= ub:
        mid = (lb + ub) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            lb = mid + 1
        else:
            ub = mid - 1

    return -1


numbers = [-1,0,3,5,9,12]
n = int(input("Enter the number you want to search for: "))

index = binary_search(numbers, n)
if index != -1:
    print(f"Found at position {index}")
else:
    print("Not found.")

"""
Question8: 

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
"""