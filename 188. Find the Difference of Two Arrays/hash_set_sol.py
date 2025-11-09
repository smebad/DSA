# Find the Difference of Two Arrays
# Hash Set Solution:
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1Set, num2Set = set(nums1), set(nums2)
        res1, res2 = [], []

        for num in num1Set:
            if num not in num2Set:
                res1.append(num)

        for num in num2Set:
            if num not in num1Set:
                res2.append(num)

        return [res1, res2]
    
# Time Complexity: O(n + m), where n and m are the lengths of nums1 and nums2 respectively. This is because we are creating sets from both arrays and then iterating through each set once.
# Space Complexity: O(n + m) in the worst case, where all elements in nums1 and nums2 are distinct. This is due to the space used by the sets num1Set and num2Set.
# This hash set solution is efficient in both time and space.


# Test Cases
# Test Case 1:
nums1 = [1,2,3]
nums2 = [2,4,6]
print(Solution().findDifference(nums1, nums2)) # Expected Output: [[1,3],[4,6]]

# Test Case 2:
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(Solution().findDifference(nums1, nums2)) # Expected Output: [[3],[]]

# Test Case 3:
nums1 = [4,5,6]
nums2 = [1,2,3]
print(Solution().findDifference(nums1, nums2)) # Expected Output: [[4,5,6],[1,2,3]]
