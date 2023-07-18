def climbStairs(n):
    # Base cases for n = 1 and n = 2
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Initialize the first two Fibonacci numbers
    first = 1
    second = 2

    # Calculate the remaining Fibonacci numbers
    for i in range(3, n+1):
        current = first + second
        first = second
        second = current

    return second
n = 5
distinct_ways = climbStairs(n)
print(distinct_ways)

"""
Question16:

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""