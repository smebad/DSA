# Container With Most Water

# Brute force solution:
from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res
    
# Time complexity: O(n^2) which means the time taken to run the code increases quadratically with the increase in the input size.
# Space complexity: O(1) which means the space taken by the code is constant and does not depend on the input size.
# Brute force solution is not optimal for large inputs as it takes O(n^2) time complexity.


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
