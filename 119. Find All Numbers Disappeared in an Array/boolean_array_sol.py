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


# Boolean Array Solution:
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mark = [False] * n

        for num in nums:
            mark[num - 1] = True

        res = []
        for i in range(1, n + 1):
            if not mark[i - 1]:
                res.append(i)
        return res

# Time Complexity: O(n), because we iterate through the list once to mark the numbers and then again to collect the missing numbers.
# Space Complexity: O(n), due to the boolean array used for marking.
# This boolean array solution is efficient and straightforward, leveraging the properties of arrays to find the missing numbers.



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