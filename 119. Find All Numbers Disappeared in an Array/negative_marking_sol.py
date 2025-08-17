# Find All Numbers Disappeared in an Array
# Negative-Markings Solution:
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)
        return res
    
# Time Complexity: O(n), because we use a single pass to mark the numbers and another pass to collect the missing numbers.
# Space Complexity: O(1), as we are modifying the input list in place and not using any additional data structures.
# This negative-markings solution is efficient and straightforward, leveraging the properties of negative marking to find the missing numbers.


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
