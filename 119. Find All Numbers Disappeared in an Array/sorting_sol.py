# Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.


# Sorting Solution:
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        res = []
        idx = 0
        for num in range(1, n + 1):
            while idx < n and nums[idx] < num:
                idx += 1
            if idx == n or nums[idx] > num:
                res.append(num)
        return res
    
# Time Complexity: O(n log n), due to the sorting step. The subsequent linear scan is O(n). Therefore, the overall time complexity is O(n log n).
# Space Complexity: O(1) if we ignore the input list, as we are not using any additional data structures that grow with input size.
# This sorting solution is also efficient and straightforward, leveraging the properties of sorting to find the missing numbers.

# Test Cases
# Test Case 1:
nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
solution1 = Solution()
output1 = solution1.findDisappearedNumbers(nums1)
print(output1)  # Expected Output: [5, 6]

# Test Case 2:
nums2 = [1, 1]
solution2 = Solution()
output2 = solution2.findDisappearedNumbers(nums2)
print(output2)  # Expected Output: [2]