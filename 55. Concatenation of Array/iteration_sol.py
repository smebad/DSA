# Concatenation of Array
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

 

# Example 1:

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:

# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]
 

# Constraints:

# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000


# Iteration Solution:
from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
    
# Time Complexity: O(n) where n is the length of the input array nums. This is because we iterate over nums once for each iteration of the outer loop.
# Space Complexity: O(n) where n is the length of the input array nums. This is because we create a new array ans that has the same length as nums.


# Test Cases:
# Test Case 1:
nums = [1,2,1]
sol = Solution()
print(sol.getConcatenation(nums))  # Output: [1,2,1,1,2,1]

# Test Case 2:
nums = [1,3,2,1]
print(sol.getConcatenation(nums))  # Output: [1,3,2,1,1,3,2,1]
