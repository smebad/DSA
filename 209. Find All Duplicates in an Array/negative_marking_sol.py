# Find All Duplicates in an Array
# Negative Marking Solution:
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                res.append(abs(num))
            nums[idx] = -nums[idx]

        return res

# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once.
# Space Complexity: O(1) excluding the output list, as we modify the input array in place.
# This negative marking solution is efficient for large input sizes due to its linear time complexity and constant space usage.


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
