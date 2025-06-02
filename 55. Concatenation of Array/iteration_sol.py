# Concatenation of Array
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
