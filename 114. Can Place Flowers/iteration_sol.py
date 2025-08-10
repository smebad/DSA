# Can Place Flowers
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
# Seen this question in a real interview before?
# 1/5
# Yes
# No


# Iteration Solution:
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1

        return n <= 0
    
# Time Complexity: O(n), where n is the length of the flowerbed array. This is because we iterate through the array once and perform a constant number of operations for each element. (flowerbed is a list of length n)
# Space Complexity: O(n), because we create a new list f that is a copy of the flowerbed list with two additional elements.
# This iterative solution is efficient and works well within the problem's constraints.

# Test Cases
solution = Solution()
# Test Case 1:
flowerbed1 = [1, 0, 0, 0, 1]
n1 = 1
print(solution.canPlaceFlowers(flowerbed1, n1))  # Output: True

# Test Case 2:
flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
print(solution.canPlaceFlowers(flowerbed2, n2))  # Output: False
