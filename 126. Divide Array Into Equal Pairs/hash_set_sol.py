# Divide Array Into Equal Pairs
# Hash-Set Solution:
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        odd_set = set()

        for num in nums:
            if num not in odd_set:
                odd_set.add(num)
            else:
                odd_set.remove(num)

        return not len(odd_set)

# Time Complexity: O(n), where n is the length of the input array. In this solution, we traverse the array once to build the set and then again to check the counts, resulting in a linear time complexity.
# Space Complexity: O(n), where n is the number of unique elements in the input array. In the worst case, we may store all elements in the set.
# This approach is efficient and works well within the given constraints.


# Test Cases
sol = Solution()

# Test Case 1:
nums1 = [3,2,3,2,2,2]
print(sol.divideArray(nums1))  # Output: True

# Test Case 2:
nums2 = [1,2,3,4]
print(sol.divideArray(nums2))  # Output: False
