# Range Sum Query - Immutable
# Prefix-Sum Solution:
class NumArray:
    def __init__(self, nums):
        self.prefix = []
        cur = 0
        for num in nums:
            cur += num
            self.prefix.append(cur)

    def sumRange(self, left, right):
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum
    
# Time Complexity: O(1) for each SumRange call, since we are using precomputed prefix sums. This is because we need to calculate the sum of a range by subtracting the left sum from the right sum.
# Space Complexity: O(n) for the prefix sum array, which stores the cumulative sums.
# This prefix-sum approach is more efficient than the brute-force solution, especially for large inputs or a high number of queries.


# Test Cases
# Test Case 1:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))  # Output: 1

# Test Case 2:
print(numArray.sumRange(2, 5))  # Output: -1

# Test Case 3:

print(numArray.sumRange(0, 5))  # Output: -3
