# Car Fleet
# Stack Solution:
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
# Time Complexity: O(nlogn) for sorting the pairs, O(n) for iterating through the pairs.
# Space Complexity: O(n) for the stack.

# Test Cases:
# Test Case 1
print(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3])) # 3

# Test Case 2
print(Solution().carFleet(10, [3], [3])) # 1

# Test Case 3
print(Solution().carFleet(100, [0,2,4], [4,2,1])) # 1
