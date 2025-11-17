# Convert an Array Into a 2D Array With Conditions
# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.

# Note that the 2D array can have a different number of elements on each row.

 

# Example 1:

# Input: nums = [1,3,4,1,2,3,1]
# Output: [[1,3,4,2],[1,3],[1]]
# Explanation: We can create a 2D array that contains the following rows:
# - 1,3,4,2
# - 1,3
# - 1
# All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
# It can be shown that we cannot have less than 3 rows in a valid array.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: [[4,3,2,1]]
# Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= nums.length
 
# HashMap Solution:
from collections import defaultdict
from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        res = []

        for num in nums:
            row = count[num]
            if len(res) == row:
                res.append([])
            res[row].append(num)
            count[num] += 1

        return res

# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once.
# Space Complexity: O(n), in the worst case, we may need to store all elements in the hashmap and the resulting 2D array.
# This hashmap-based solution efficiently groups the elements into rows while ensuring that each row contains distinct integers.


# Test Cases:
sol = Solution()

# Test Case 1:
nums1 = [1,3,4,1,2,3,1]
print(sol.findMatrix(nums1))  # Expected output: [[1,3,4,2],[1,3],[1]]

# Test Case 2:
nums2 = [1,2,3,4]
print(sol.findMatrix(nums2))  # Expected output: [[4,3,2,1]]