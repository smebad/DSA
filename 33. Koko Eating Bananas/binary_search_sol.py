# Koko Eating Bananas
# Binary search Solution:

from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
    
# Time Complexity: O(n * log(m)) where n is the number of piles and m is the maximum number of bananas in a pile. Which is the maximum speed we can have. log(m) is the number of iterations in the binary search.
# Space Complexity: O(1) as we are using only a constant amount of space.
# The binary search solution is more efficient than the brute force solution as it narrows down the search space for the minimum speed using the properties of the problem.


# Test Cases:
# Test Case 1:
piles = [3,6,7,11]
h = 8
print(Solution().minEatingSpeed(piles, h)) # Expected Output: 4

# Test Case 2:
piles = [30,11,23,4,20]
h = 5
print(Solution().minEatingSpeed(piles, h)) # Expected Output: 30

# Test Case 3:
piles = [30,11,23,4,20]
h = 6
print(Solution().minEatingSpeed(piles, h)) # Expected Output: 23
