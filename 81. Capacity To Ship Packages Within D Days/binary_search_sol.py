# Capacity To Ship Packages Within D Days
# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 

# Example 1:

# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
# Example 2:

# Input: weights = [3,2,2,4,1,4], days = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
# Example 3:

# Input: weights = [1,2,3,1,1], days = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1
 

# Constraints:

# 1 <= days <= weights.length <= 5 * 104
# 1 <= weights[i] <= 500


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