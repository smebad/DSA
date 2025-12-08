# Find All Duplicates in an Array
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.

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