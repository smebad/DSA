# Find Minimum in Rotated Sorted Array
# Brute Force Solution:

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
    
# Time Complexity: O(n)
# Space Complexity: O(1)
# The brute force solution is to simply find the minimum element in the array using the built-in min function. This approach has a time complexity of O(n) because it needs to iterate through all elements in the array to find the minimum. The space complexity is O(1) since we are not using any additional data structures that grow with the input size.
# However, this approach does not meet the requirement of O(log n) time complexity.
# To achieve O(log n) time complexity, we can use a binary search approach. The idea is to find the pivot point where the array is rotated and then return the minimum element based on the pivot point. This approach has a time complexity of O(log n) and a space complexity of O(1).


# Test Cases:
# Test Case 1:
nums = [3,4,5,1,2]
sol = Solution()
print(sol.findMin(nums))  # Output: 1

# Test Case 2:
nums = [4,5,6,7,0,1,2]
sol = Solution()
print(sol.findMin(nums))  # Output: 0

# Test Case 3:
nums = [11,13,15,17]
sol = Solution()
print(sol.findMin(nums))  # Output: 11
