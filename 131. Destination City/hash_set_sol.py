# Destination City
# Hash-Set Solution:
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        for p in paths:
            s.add(p[0])

        for p in paths:
            if p[1] not in s:
                return p[1]

# Time Complexity: O(n), where n is the number of paths. In this approach, we use a hash set to store all the starting cities, allowing for O(1) average time complexity when checking if a city is a starting point.
# Space Complexity: O(n), where n is the number of paths. In the worst case, we store all starting cities in the hash set.
# This solution is efficient and works well within the given constraints.


# Test Cases
sol = Solution()

# Test Case 1:
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(sol.destCity(paths))  # Output: "Sao Paulo"

# Test Case 2:
paths = [["B","C"],["D","B"],["C","A"]]
print(sol.destCity(paths))  # Output: "A"

# Test Case 3:
paths = [["A","Z"]]
print(sol.destCity(paths))  # Output: "Z"

