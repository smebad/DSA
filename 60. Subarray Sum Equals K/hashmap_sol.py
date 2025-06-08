# Subarray Sum Equals K
# Hash Map Solution:

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
        return res
    
# Time Complexity: O(n) where n is the length of nums array. Subarray sum is calculated for each element in nums array.
# Space Complexity: O(n) where n is the length of nums array. We are using a dictionary to store the prefix sums.


# Test Cases:
# Test Case 1:
nums = [1,1,1]
k = 2
sol = Solution()
print(sol.subarraySum(nums, k))  # Output: 2

# Test Case 2:
nums = [1,2,3]
k = 3
sol = Solution()
print(sol.subarraySum(nums, k))  # Output: 2
