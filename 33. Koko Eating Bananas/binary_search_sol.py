# Koko Eating Bananas
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109


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