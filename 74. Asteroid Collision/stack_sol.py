# Asteroid Collision
# Stack Solution:
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack
    
# Time Complexity: O(n) where n is the number of asteroids. This is because we are iterating through the asteroids once and performing constant time operations for each asteroid.
# Space Complexity: O(n) in the worst case where no collisions occur, and all asteroids are stored in the stack.
# The stack can grow to the size of the input list in the worst case.
# This stack solution efficiently handles the collisions by using a stack to keep track of the asteroids that are still in play. When a new asteroid is processed, it checks for collisions with the top of the stack and resolves them accordingly. If no collision occurs, the asteroid is added to the stack. This approach ensures that we only traverse the list of asteroids once, making it efficient for large inputs.


# Test cases
# Test Case 1:
asteroids1 = [5, 10, -5]
solution1 = Solution()
print(solution1.asteroidCollision(asteroids1))  # Output: [5, 10]

# Test Case 2:
asteroids2 = [8, -8]
solution2 = Solution()
print(solution2.asteroidCollision(asteroids2))  # Output: []

# Test Case 3:
asteroids3 = [10, 2, -5]
solution3 = Solution()
print(solution3.asteroidCollision(asteroids3))  # Output: [10]
