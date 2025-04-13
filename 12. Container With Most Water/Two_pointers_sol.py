# Container With Most Water
# Two Pointers solution:
from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
    
# Time complexity: O(n) which means the time taken to run the code increases linearly with the increase in the input size.
# Space complexity: O(1) which means the space taken by the code is constant and does not depend on the input size.
# Two pointers solution is optimal for large inputs as it takes O(n) time complexity.


# Test Cases:
# Test Case 1:
heights = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(heights)) # Expected Output: 49

# Test Case 2:
heights = [1,1]
print(Solution().maxArea(heights)) # Expected Output: 1

# Test Case 3:
heights = [4,3,2,1,4]
print(Solution().maxArea(heights)) # Expected Output: 16
