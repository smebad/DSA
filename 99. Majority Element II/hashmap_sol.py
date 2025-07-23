# Majority Element II
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow up: Could you solve the problem in linear time and in O(1) space?


# Hashmap solution:
from collections import defaultdict
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
            
            if len(count) <= 2:
                continue
            
            new_count = defaultdict(int)
            for num, c in count.items():
                if c > 1:
                    new_count[num] = c - 1
            count = new_count
        
        res = []
        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        
        return res
    
# Time Complexity: O(n) where n is the length of nums. This is because we iterate through the list once to build the count dictionary and then again to filter the results.
# Space Complexity: O(1) in terms of the number of unique elements stored in the count dictionary, which can be at most 2 for this problem.
# This hashmap solution is efficient for the problem constraints and handles the majority element condition effectively.

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
