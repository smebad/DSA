# Kth Largest Element in an Array
# Sorting Solution:

from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
    
  
# Time Complexity: O(n log n) where n is the length of nums. This is due to the sorting operation.
# Space Complexity: O(1) or O(n) depending on the sorting algorithm used.
# In Python, the built-in sort function uses Timsort which has a space complexity of O(n) in the worst case.
# This solution is efficient and works well within the constraints given (1 <= k <= nums.length <= 10^5) but in question it was asked to solve it without sorting.


# Test Cases:
# Test Case 1:
nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))  # Output: 5

# Test Case 2:
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(Solution().findKthLargest(nums, k))  # Output: 4
