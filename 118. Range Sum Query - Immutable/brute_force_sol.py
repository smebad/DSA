# Range Sum Query - Immutable
# Brute-Force Solution:
class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        res = 0
        for i in range(left, right + 1):
            res += self.nums[i]
        return res
    
# Time Complexity: O(n) for each SumRange call, where n is the number of elements in the range. This is because we need to iterate through the range to calculate the sum.
# Space Complexity: O(1) since we are using a constant amount of space.
# This brute-force solution is not efficient for large inputs or a high number of queries.


# Test Cases
# Test Case 1:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))  # Output: 1

# Test Case 2:
print(numArray.sumRange(2, 5))  # Output: -1

# Test Case 3:

print(numArray.sumRange(0, 5))  # Output: -3
