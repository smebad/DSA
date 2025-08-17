# Find All Numbers Disappeared in an Array
# Hash-Set Solution:
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        store = set(range(1, n + 1))

        for num in nums:
            store.discard(num)

        return list(store)
    
# Time Complexity: O(n), where n is the length of the input list nums. This is because we iterate through the list once to populate the set and then again to convert the set to a list.
# Space Complexity: O(n), because we use a set to store the numbers in the range [1, n].
# This hash-set solution is efficient and straightforward, leveraging the properties of sets to find the missing numbers.


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
