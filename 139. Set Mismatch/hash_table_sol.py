# Set Mismatch
# Hash Table Solution:
from typing import List
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0] # [duplicate, missing]
        count = Counter(nums)

        for i in range(1, len(nums) + 1):
            if count[i] == 0:
                res[1] = i
            if count[i] == 2:
                res[0] = i

        return res

# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once to count the occurrences of each number and then again to find the duplicate and missing numbers.
# Space Complexity: O(n), in the worst case, we may need to store counts for all n numbers in the Counter dictionary.
# This hash table solution efficiently identifies the duplicate and missing numbers by leveraging the counting capabilities of the Counter class from the collections module.


# Test Cases
sol = Solution()

# Test Case 1:
nums = [1, 2, 2, 4]
print(sol.findErrorNums(nums))  # Output: [2, 3]

# Test Case 2:
nums = [1, 1]
print(sol.findErrorNums(nums))  # Output: [1, 2]
