# 3Sum

# Brute Force Solution:
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]
    
# Time Complexity: O(n^3) which means the time taken by the algorithm increases cubically with the increase in the number of elements in the input list.
# Space Complexity: O(m) where m is the number of unique triplets found. In the worst case, it can be O(n) if all elements are unique and form a triplet.
# This is not an efficient solution and can be improved using two pointers or hash map approach.

# Test Cases:
# Test Case 1:
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums)) # Expected Output: [[-1,-1,2],[-1,0,1]]

# Test Case 2:
nums = [0,1,1]
print(Solution().threeSum(nums)) # Expected Output: []

# Test Case 3:
nums = [0,0,0]
print(Solution().threeSum(nums)) # Expected Output: [[0,0,0]]
