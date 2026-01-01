# Remove Duplicates from Sorted Array II
# Two Pointers Solution:
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1

            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1

        return l

# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once with the right pointer.
# Space Complexity: O(1), since we are modifying the input array in place and using only a constant amount of extra space.
# This solution is efficient and meets the problem's constraints.


# Test Cases:
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = solution.removeDuplicates(nums1)
    print(f"Output: {k1}, nums = {nums1[:k1]}")  # Expected: Output: 5, nums = [1, 1, 2, 2, 3]

    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k2 = solution.removeDuplicates(nums2)
    print(f"Output: {k2}, nums = {nums2[:k2]}")  # Expected: Output: 7, nums = [0, 0, 1, 1, 2, 3, 3]
