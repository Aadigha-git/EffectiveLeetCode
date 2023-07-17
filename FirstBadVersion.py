def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left
# Example usage with a mock implementation of isBadVersion()
def isBadVersion(version):
    # Assume version 4 is the first bad version
    if version >= 1:
        return True
    return False

n = 1
first_bad = firstBadVersion(n)
print(first_bad)  # Output: 4
