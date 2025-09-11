# Set Mismatch
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104

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