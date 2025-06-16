# Boats to Save People
# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

 

# Example 1:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
 

# Constraints:

# 1 <= people.length <= 5 * 104
# 1 <= people[i] <= limit <= 3 * 104


# Sorting + Two Pointers Solution:
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res
    
# Time Complexity: O(n log n) because of sorting and O(n) for iterating through the array.
# Space Complexity: O(1) or O(n) if we consider the output array as part of the input.
# This solution is efficient in terms of both time and space complexity and can be difficult to understand but this is the best solution for this problem.


# Test Cases
# Test Case 1:
print(Solution().numRescueBoats([1,2], 3)) # -> 1

# Test Case 2:
print(Solution().numRescueBoats([3,2,2,1], 3)) # -> 3

# Test Case 3:
print(Solution().numRescueBoats([3,5,3,4], 5)) # -> 4
