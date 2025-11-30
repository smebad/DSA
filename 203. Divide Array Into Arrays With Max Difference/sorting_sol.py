# Divide Array Into Arrays With Max Difference
# Sorting Solution:
from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            res.append(nums[i: i + 3])

        return res

# Time Complexity: O(n log n), where n is the length of the input array nums. This is due to the sorting step.
# Space Complexity: O(n) for storing the result array.
# This sorting solution is efficient and straightforward, leveraging the properties of sorted arrays to ensure that the maximum difference condition is met within each group of three elements.


# Test cases
sol = Solution()

# Test case 1:
nums1 = [1,3,4,8,7,9,3,5,1]
k1 = 2
print(sol.divideArray(nums1, k1))  # Output: [[1,1,3],[3,4,5],[7,8,9]]

# Test case 2:
nums2 = [2,4,2,2,5,2]
k2 = 2
print(sol.divideArray(nums2, k2))  # Output: []

# Test case 3:
nums3 = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]
k3 = 14
print(sol.divideArray(nums3, k3))  # Output: [[2,2,2],[4,5,5],[5,5,7],[7,8,8],[9,9,10],[11,12,12]]
