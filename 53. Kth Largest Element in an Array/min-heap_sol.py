# Kth Largest Element in an Array
# Min-Heap Solution:

import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
  
# Time Complexity: O(n log k) where n is the length of nums and k is the value of k. This is due to the use of a min-heap to find the kth largest element.
# Space Complexity: O(k) where k is the value of k. This is due to the use of a min-heap to find the kth largest element.
# In Python, the heapq module uses a min-heap data structure, which has a space complexity of O(k) in the worst case.
# This solution is efficient and works well within the constraints given (1 <= k <= nums.length <= 105) this is not the fully sorting solution rather it uses a min-heap to find the kth largest element.

# Test Cases:
# Test Case 1:
nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))  # Output: 5

# Test Case 2:
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(Solution().findKthLargest(nums, k))  # Output: 4
