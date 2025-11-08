# Count Negative Numbers
# Count Negative Numbers Solution:
from typing import List

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        neg = 0
        for num in nums:
            if num == 0:
                return 0
            neg += (1 if num < 0 else 0)
        return -1 if neg % 2 else 1
    
# Time Complexity: O(n), where n is the number of elements in the input array nums.
# Space Complexity: O(1), as we are using a constant amount of extra space.
# This solution is efficient and works well within the given constraints.


# Test Cases:
sol = Solution()

# Test Case 1:
nums1 = [-1,-2,-3,-4,3,2,1]
print(sol.arraySign(nums1))  # Output: 1

# Test Case 2:
nums2 = [1,5,0,2,-3]
print(sol.arraySign(nums2))  # Output: 0

# Test Case 3:
nums3 = [-1,1,-1,1,-1]
print(sol.arraySign(nums3))  # Output: -1
