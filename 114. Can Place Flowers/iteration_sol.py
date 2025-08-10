# Can Place Flowers
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

