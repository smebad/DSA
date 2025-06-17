# Contains Duplicate II
# Hash Set Solution:
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        
        return False
    
# Time Complexity: O(n) where n is the length of the nums array. This is because we are iterating through the nums array once.
# Space Complexity: O(min(n, k)) where n is the length of the nums array and k is the value of k. This is because we are using a hash set to keep track of the elements in the window.
# This solution is efficient for large inputs as it has a time complexity of O(n). It is optimal and works well for the problem.


# Test Cases
# Test Case 1:
nums = [1,2,3,1]
k = 3
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))  # Output: True

# Test Case 2:
nums = [1,0,1,1]
k = 1
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))  # Output: True

# Test Case 3:
nums = [1,2,3,1,2,3]
k = 2
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))  # Output: False
