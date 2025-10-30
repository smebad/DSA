# Brick Wall
# There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

# Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

# Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

 

# Example 1:


# Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Output: 2
# Example 2:

# Input: wall = [[1],[1],[1]]
# Output: 3
 

# Constraints:

# n == wall.length
# 1 <= n <= 104
# 1 <= wall[i].length <= 104
# 1 <= sum(wall[i].length) <= 2 * 104
# sum(wall[i]) is the same for each row i.
# 1 <= wall[i][j] <= 231 - 1

# HashMap Solution:
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0: 0}

        for r in wall:
            total = 0
            for i in range(len(r) - 1):
                total += r[i]
                countGap[total] = 1 + countGap.get(total, 0)

        return len(wall) - max(countGap.values())
    
# Time Complexity: O(n), where n is the total number of bricks in the wall. We iterate through the wall once to count the gaps between the bricks.
# Space Complexity: O(g), where g is the number of unique gaps between bricks. In the worst case, this could be O(n) if every brick ends at a different position.
# This hashmap solution is efficient and works well within the given constraints.


# Test Cases:
sol = Solution()

# Test Case 1
wall1 = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(sol.leastBricks(wall1))  # Expected output: 2

# Test Case 2
wall2 = [[1],[1],[1]]
print(sol.leastBricks(wall2))  # Expected output: 3
