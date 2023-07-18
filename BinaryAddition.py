def addBinary(x, y):
    int_x = int(x, 2)
    int_y = int(y, 2)

    int_sum = int_x+int_y

    binary_sum = bin(int_sum)[2:]

    return binary_sum
    
x = input("Enter number 1: ")
y = input("Enter number 2: ")

sum = addBinary(x, y)

print(sum)

"""
Question20:

Given two binary strings a and b, return their sum as a binary string.
"""