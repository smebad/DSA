# Largest Number
# Sorting Solution:
from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))
    
# Time Complexity: O(n log n) where n is the number of elements in nums. This is due to the sorting step.
# Space Complexity: O(n) for storing the string representations of the numbers. This is because the largest number can be of length n.
# This sorting solution is efficient and works well within the given constraints.


# Test Cases:
sol = Solution()

# Test Case 1:
nums1 = [10, 2]
print(sol.largestNumber(nums1))  # Output: "210"

# Test Case 2:
nums2 = [3, 30, 34, 5, 9]
print(sol.largestNumber(nums2))  # Output: "9534330"

# Test Case 3:
nums3 = [0, 0]
print(sol.largestNumber(nums3))  # Output: "0"
