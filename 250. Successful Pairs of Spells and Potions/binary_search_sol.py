# Successful Pairs of Spells and Potions
# Binary Search + Sorting Solution:
from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []

        for s in spells:
            l, r = 0, len(potions) - 1
            idx = len(potions)

            while l <= r:
                m = (l + r) // 2
                if s * potions[m] >= success:
                    r = m - 1
                    idx = m
                else:
                    l = m + 1

            res.append(len(potions) - idx)

        return res

# Time Complexity: O(n log m), where n is the number of spells and m is the number of potions. Sorting the potions takes O(m log m) time, and for each spell, we perform a binary search on the potions which takes O(log m) time.
# Space Complexity: O(1) if we don't consider the output array, as we are using a constant amount of extra space.
# This binary search + sorting approach efficiently finds the number of successful pairs for each spell by leveraging the sorted order of potions.


# Test Cases:
# Test Case 1
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(Solution().successfulPairs(spells, potions, success)) # Output: [4,0,3]

# Test Case 2
spells = [3,1,2]
potions = [8,5,8]
success = 16
print(Solution().successfulPairs(spells, potions, success)) # Output: [2,0,2]
