# Container With Most Water
# Medium
# Topics
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


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