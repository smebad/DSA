# Path Crossing
# Hash Set Solution:

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir = {
            'N': [0, 1],
            'S': [0, -1],
            'E': [1, 0],
            'W': [-1, 0]
        }

        visit = set()
        x, y = 0, 0

        for c in path:
            visit.add((x, y))
            dx, dy = dir[c]
            x, y = x + dx, y + dy
            if (x, y) in visit:
                return True

        return False
    
# Time Complexity: O(n), where n is the length of the path. We iterate through each character in the path once.
# Space Complexity: O(n), in the worst case, we may visit all unique points and store them in the set.
# This approach efficiently checks for path crossings using a hash set to track visited coordinates.


# Test Cases
solution = Solution()

# Test Case 1:
path = "NES"
print(solution.isPathCrossing(path)) # False

# Test Case 2:
path = "NESWW"
print(solution.isPathCrossing(path)) # True
