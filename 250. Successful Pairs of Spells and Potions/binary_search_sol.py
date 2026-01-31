
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

# Example 1:
# Successful Pairs of Spells and Potions
# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.
# Example 2:

# Input: spells = [3,1,2], potions = [8,5,8], success = 16
# Output: [2,0,2]
# Explanation:
# - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
# - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
# - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
# Thus, [2,0,2] is returned.
 

# Constraints:

# n == spells.length
# m == potions.length
# 1 <= n, m <= 105
# 1 <= spells[i], potions[i] <= 105
# 1 <= success <= 1010

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