# Divide Array Into Equal Pairs
# Hash-Map Solution:
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        for cnt in count.values():
            if cnt % 2 == 1:
                return False

        return True

# Time Complexity: O(n), where n is the length of the input array. In this solution, we traverse the array once to build the frequency map and then again to check the counts, resulting in a linear time complexity.
# Space Complexity: O(n), where n is the number of unique elements in the input array. In the worst case, we may store all elements in the frequency map.
# This approach is efficient and works well within the given constraints.


# Test Cases
sol = Solution()

# Test Case 1:
nums1 = [3,2,3,2,2,2]
print(sol.divideArray(nums1))  # Output: True

# Test Case 2:
nums2 = [1,2,3,4]
print(sol.divideArray(nums2))  # Output: False
