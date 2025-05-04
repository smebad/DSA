# Find the Duplicate Number
# Fast and Slow Pointers solution:
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
    
# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(1), since we are using only a constant amount of space for the two pointers.
# The algorithm uses a cycle detection method (Floyd's Tortoise and Hare) to find the duplicate number.
# What is Floyd's Tortoise and Hare algorithm? Floyd's Tortoise and Hare algorithm is a pointer algorithm that uses two pointers, one moving at twice the speed of the other. If there is a cycle in the linked list, the fast pointer will eventually meet the slow pointer. If there is no cycle, the fast pointer will reach the end of the list.
# In this case, we are using it to find the duplicate number in the array.
# The first part of the algorithm finds the intersection point of the two pointers, and the second part finds the entrance to the cycle (the duplicate number).
# However, this solution is not modifying the input array and is using only constant extra space, which is a requirement of the problem.
# This solution is efficient and works well for the problem.

# Test Cases:
# Test case 1:
nums = [1, 3, 4, 2, 2]
sol = Solution()
print(sol.findDuplicate(nums))  # Output: 2

# Test case 2:
nums = [3, 1, 3, 4, 2]
sol = Solution()
print(sol.findDuplicate(nums))  # Output: 3

# Test case 3:
nums = [3, 3, 3, 3, 3]
sol = Solution()
print(sol.findDuplicate(nums))  # Output: 3
