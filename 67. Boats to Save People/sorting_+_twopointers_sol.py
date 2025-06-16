# Boats to Save People
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
