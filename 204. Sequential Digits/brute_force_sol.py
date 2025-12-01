# Sequential Digits
# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
 

# Constraints:

# 10 <= low <= high <= 10^9

# Brute Force Solution:
from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        for num in range(low, high + 1):
            s = str(num)
            flag = True
            for i in range(1, len(s)):
                if ord(s[i]) - ord(s[i - 1]) != 1:
                    flag = False
                    break
            if flag:
                res.append(num)

        return res
    
# Time Complexity: O(n), where n is the number of integers in the range [low, high]. We iterate through each integer in the range and check if it has sequential digits.
# Space Complexity: O(1), as we only use a constant amount of space to store the result.
# This brute force solution may not be efficient for large ranges, but it is straightforward and easy to understand.


# Test Cases
sol = Solution()

# Test Case 1:
low1 = 100
high1 = 300
print(sol.sequentialDigits(low1, high1))  # Output: [123, 234]

# Test Case 2:
low2 = 1000
high2 = 13000
print(sol.sequentialDigits(low2, high2))  # Output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]