# Brick Wall
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
