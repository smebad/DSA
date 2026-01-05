# Contiguous Array
# Hashmap Solution:
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero = one = res = 0
        diff_index = {}

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1

            if one - zero not in diff_index:
                diff_index[one - zero] = i

            if one == zero:
                res = one + zero
            else:
                idx = diff_index[one - zero]
                res = max(res, i - idx)

        return res

# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once, performing constant-time operations for each element.
# Space Complexity: O(n) in the worst case, where we store the differences in the hashmap. In the best case, the space complexity can be O(1) if all elements are the same.
# This solution is efficient and works well within the given constraints.


# Test Cases:
sol = Solution()

# Test Case 1:
nums1 = [0, 1]
print(sol.findMaxLength(nums1))  # Output: 2

# Test Case 2:
nums2 = [0, 1, 0]
print(sol.findMaxLength(nums2))  # Output: 2

# Test Case 3:
nums3 = [0, 1, 1, 1, 1, 1, 0, 0, 0]
print(sol.findMaxLength(nums3))  # Output: 6
