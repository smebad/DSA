# Search in Rotated Sorted Array
# Binary Search One Pass Solution:

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
    
# Time Complexity: O(log n) because we are using binary search and we are reducing the search space by half in each iteration
# Space Complexity: O(1) because we are not using any additional data structures
# The algorithm uses two pointers (l and r) to keep track of the search space, and a mid pointer to find the middle element in each iteration. The algorithm checks if the target is in the left or right half of the array and adjusts the pointers accordingly. The algorithm continues until the target is found or the search space is empty.
# The algorithm has a time complexity of O(log n) because it reduces the search space by half in each iteration, and a space complexity of O(1) because it only uses a constant amount of extra space for the pointers.
# This binary search one pass solution is efficient and works well for the problem of searching in a rotated sorted array. It is a common interview question and is often asked in technical interviews for software engineering positions. The algorithm is also used in various applications, such as searching in databases and finding elements in sorted arrays.


# Test Cases:
# Test Case 1: 
nums = [4,5,6,7,0,1,2] 
target = 0
print(Solution().search(nums, target)) # Output: 4

# Test Case 2:
nums = [4,5,6,7,0,1,2]
target = 3
print(Solution().search(nums, target)) # Output: -1

# Test Case 3:
nums = [1]
target = 0
print(Solution().search(nums, target)) # Output: -1
