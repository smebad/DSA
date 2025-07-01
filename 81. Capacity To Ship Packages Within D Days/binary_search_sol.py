# Capacity To Ship Packages Within D Days
# Binary Search Solution:
from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap

                currCap -= w
            return True

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res
    
# Time Complexity: O(n log n) where n is the number of weights. This is because we perform a binary search on the range of possible capacities (from max(weights) to sum(weights)), and for each capacity, we check if it can ship the packages within the given days, which takes O(n) time.
# Space Complexity: O(1) since we are using a constant amount of space for variables. This does not depend on the size of the input weights list.
# This binary search solution is optimal for large inputs as it takes O(n log n) time complexity

# Test Cases
# Test Case 1:
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(Solution().shipWithinDays(weights, days)) # Expected Output: 15

# Test Case 2:
weights = [3,2,2,4,1,4]
days = 3
print(Solution().shipWithinDays(weights, days)) # Expected Output: 6

# Test Case 3:
weights = [1,2,3,1,1]
days = 4
print(Solution().shipWithinDays(weights, days)) # Expected Output: 3
