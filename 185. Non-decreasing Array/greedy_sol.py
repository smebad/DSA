# Non-decreasing Array
# Greedy Solution:
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            if changed:
                return False
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
            changed = True
        return True
    
# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once.
# Space Complexity: O(1), as we use only a constant amount of extra space.
# This greedy solution is efficient and effectively checks if the array can be made non-decreasing by modifying at most one element.


# Test Cases:
sol = Solution()

# Test Case 1
print(sol.checkPossibility([4, 2, 3]))  # Expected output: True

# Test Case 2
print(sol.checkPossibility([4, 2, 1]))  # Expected output: False
