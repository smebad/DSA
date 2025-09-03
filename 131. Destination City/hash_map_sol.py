# Destination City
# Hash Map Solution:
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp = {p[0]: p[1] for p in paths}

        start = paths[0][0]
        while start in mp:
            start = mp[start]
        return start

# Time Complexity: O(n), where n is the number of paths. In this approach, we use a hash map to store all the starting cities and their corresponding destination cities, allowing for O(1) average time complexity when checking if a city is a starting point.
# Space Complexity: O(n), where n is the number of paths. In the worst case, we store all starting cities and their destinations in the hash map.
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

