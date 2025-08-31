# Number of Good Pairs
# Hash-Map Solution:
from typing import List
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0
        for num in nums:
            res += count[num]
            count[num] += 1
        return res

# Time Complexity: O(n), where n is the length of the input array. In this case, we are using a hash map to count the pairs.
# Space Complexity: O(n), where n is the number of unique elements in the input array.
# This solution is more efficient than the brute force approach, especially for larger input sizes.

# Test Cases
sol = Solution()

# Test Case 1:
nums = [1,2,3,1,1,3]
print(sol.numIdenticalPairs(nums))  # Output: 4

# Test Case 2:
nums = [1,1,1,1]
print(sol.numIdenticalPairs(nums))  # Output: 6

# Test Case 3:
nums = [1,2,3]
print(sol.numIdenticalPairs(nums))  # Output: 0

