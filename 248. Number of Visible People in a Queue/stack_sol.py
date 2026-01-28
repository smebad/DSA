# Number of Visible People in a Queue
# Stack Solution:
from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] < heights[i]:
                stack.pop()
                res[i] += 1

            if stack:
                res[i] += 1
            stack.append(heights[i])

        return res

# Time Complexity: O(n), where n is the number of people in the queue. Each person is pushed and popped from the stack at most once.
# Space Complexity: O(n) in the worst case, where the stack can hold all the people in the queue.
# This stack solution is efficient and works well within the given constraints.


# Test Cases:
# Test Case 1:
heights = [10,6,8,5,11,9]
print(Solution().canSeePersonsCount(heights)) # Expected Output: [3,1,2,1,1,0]
