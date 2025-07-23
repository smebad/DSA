# Majority Element II
# Sorting solution:
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        res, n = [], len(nums)
        
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[i] == nums[j]:
                j += 1
            if (j - i) > n // 3:
                res.append(nums[i])
            i = j

        return res
    
# Time Complexity: O(n log n) where n is the length of nums. This is due to the sorting step, which is the most time-consuming operation in this solution.
# Space Complexity: O(1) if we consider the output list as the only additional space used, otherwise O(n) for the input list.
# This solution is not optimal in terms of time complexity compared to the hashmap solution, but it is straightforward and easy to understand.

# Test cases
# Test Case 1:
nums1 = [3, 2, 3]
solution1 = Solution()
print(solution1.majorityElement(nums1))  # Output: [3]

# Test Case 2:
nums2 = [1]
solution2 = Solution()
print(solution2.majorityElement(nums2))  # Output: [1]

# Test Case 3:
nums3 = [1, 2]
solution3 = Solution()
print(solution3.majorityElement(nums3))  # Output: [1, 2]
