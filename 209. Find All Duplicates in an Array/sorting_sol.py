# Find All Duplicates in an Array
# Sorting Solution:
from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                res.append(nums[i])

        return res

# Time Complexity: O(n log n) where n is the length of the input array nums. This is due to the sorting step.
# Space Complexity: O(1) excluding the output list, as we are sorting the array in place.
# This sorting solution is straightforward but may be less efficient for very large input sizes compared to the negative marking solution.

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [4,3,2,7,8,2,3,1]
    print(solution.findDuplicates(nums1))  # Expected output: [2, 3]

    # Test Case 2
    nums2 = [1,1,2]
    print(solution.findDuplicates(nums2))  # Expected output: [1]

    # Test Case 3
    nums3 = [1]
    print(solution.findDuplicates(nums3))  # Expected output: []
