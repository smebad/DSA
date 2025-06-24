# Asteroid Collision
# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

# Constraints:

# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0


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
