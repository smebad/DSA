# Koko Eating Bananas
# Brute Force Solution:

from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile + speed - 1) // speed
            
            if totalTime <= h:
                return speed
            speed += 1
        return speed
    
# Time Complexity: O(n * m) where n is the number of piles and m is the maximum number of bananas in a pile.
# Space Complexity: O(1) as we are using only a constant amount of space.
# The brute force solution is not efficient for large inputs, as it checks every possible speed from 1 to the maximum number of bananas in a pile. However, it is a simple and straightforward approach to solve the problem. The solution can be improved using binary search to find the minimum speed more efficiently.


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
