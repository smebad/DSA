# Next Greater Element I
# Stack Solution:
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {num : i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res
    
# Time Complexity: O(m * n) where m is the length of nums1 and n is the length of nums2. This is because we traverse nums2 once and for each element, we may pop elements from the stack.
# Space Complexity: O(m) as in stack we store elements from nums1 that we encounter in nums2. The result array also takes O(m) space.
# This solution is optimal for the given constraints and efficiently finds the next greater element using a stack.


# Test Cases
# Test Case 1:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution().nextGreaterElement(nums1, nums2))  # Expected Output: [-1, 3, -1]

# Test Case 2:
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(Solution().nextGreaterElement(nums1, nums2))  # Expected Output: [3, -1]
