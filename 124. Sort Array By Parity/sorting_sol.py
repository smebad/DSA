# Sort Array By Parity
# Sorting Solution:
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x: x & 1)
        return nums
    
# Time Complexity: O(n log n) due to the sorting operation. This is because sorting takes O(n log n) time in the worst case.
# Space Complexity: O(1) or O(n) depending on the sorting algorithm used.
# This sorting approach is not optimal for this problem since we only need to partition the array into evens and odds.


# Test Cases
sol = Solution()
# Test Case 1:
nums1 = [3,1,2,4]
print(sol.sortArrayByParity(nums1))  # Output: [2,4,3,1] or any valid arrangement

# Test Case 2:
nums2 = [0]

print(sol.sortArrayByParity(nums2))  # Output: [0]
