# Destination City
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

# Example 1:

# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
# Example 2:

# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are: 
# "D" -> "B" -> "C" -> "A". 
# "B" -> "C" -> "A". 
# "C" -> "A". 
# "A". 
# Clearly the destination city is "A".
# Example 3:

# Input: paths = [["A","Z"]]
# Output: "Z"
 

# Constraints:

# 1 <= paths.length <= 100
# paths[i].length == 2
# 1 <= cityAi.length, cityBi.length <= 10
# cityAi != cityBi
# All strings consist of lowercase and uppercase English letters and the space character.


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
