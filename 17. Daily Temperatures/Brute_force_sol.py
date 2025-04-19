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


# Brute force solution:
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []

        for i in range(n):
            count = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1
            count = 0 if j == n else count
            res.append(count)
        return res
    
# Time complexity: O(n^2) where n is the length of the temperatures array. This is because we are iterating through the temperatures array twice, once to find the next warmer day and once to count the number of days.
# Space complexity: O(n) where n is the length of the temperatures array. This is because we are using a new array res to store the result.
# This is not the most efficient solution, but it is a brute force solution that works for small inputs.
# The time complexity can be improved to O(n) using a stack-based approach, which is more efficient for larger inputs.


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