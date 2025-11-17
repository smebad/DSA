# Convert an Array Into a 2D Array With Conditions
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
