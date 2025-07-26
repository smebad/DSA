# Next Greater Element I
# Hash Map Solution:
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {num : i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res
    
# Time Complexity: O(m * n) where m is the length of nums1 and n is the length of nums2. This is because for each element in nums2, we may need to traverse the remaining elements to find the next greater element.
# Space Complexity: O(m) for storing the indices of elements in nums1 in a hash map. The result array also takes O(m) space.
# This solution is straightforward and optimal for the given constraints, but it can be improved to O(m + n) using a stack-based approach.

# Test Cases
# Test Case 1:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution().nextGreaterElement(nums1, nums2))  # Expected Output: [-1, 3, -1]

# Test Case 2:
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(Solution().nextGreaterElement(nums1, nums2))  # Expected Output: [3, -1]
