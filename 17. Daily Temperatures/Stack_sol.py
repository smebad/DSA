# Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


# Stack solution:
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
    
# Time complexity: O(n) where n is the length of the temperatures array. This is because we are iterating through the temperatures array once and using a stack to keep track of the indices of the temperatures.
# Space complexity: O(n) where n is the length of the temperatures array. This is because we are using a stack to keep track of the indices of the temperatures.
# This is the most efficient solution for this problem, as it uses a stack to keep track of the indices of the temperatures and only iterates through the temperatures array once.
# This solution is efficient for larger inputs and has a linear time complexity.


# Test Cases:
# Test Case 1:
temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))  # Output: [1,1,4,2,1,1,0,0]

# Test Case 2:
temperatures = [30,40,50,60]
print(Solution().dailyTemperatures(temperatures))  # Output: [1,1,1,0]

# Test Case 3:
temperatures = [30,60,90]
print(Solution().dailyTemperatures(temperatures))  # Output: [1,1,0]