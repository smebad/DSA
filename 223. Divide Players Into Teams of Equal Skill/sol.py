# Divide Players Into Teams of Equal Skill
# Solution:
from typing import List
from collections import Counter

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)

        if (2 * total) % len(skill):
            return -1
        
        count = Counter(skill)
        target = (2 * total) // len(skill)
        res = 0

        for s in skill:
            if not count[s]:
                continue
            
            count[s] -= 1
            diff = target - s
            if not count[diff]:
                return -1
            
            res += s * diff
            count[diff] -= 1
        
        return res

# Time Complexity: O(n), where n is the number of players. We traverse the skill list once and perform constant time operations for each player.
# Space Complexity: O(k), where k is the range of skill values (maximum skill value - minimum skill value). We use a Counter to store the frequency of each skill level.
# This solution is efficient and works well within the given constraints.


# Test Cases:
solution = Solution()
skill1 = [3,2,5,1,3,4]
print(solution.dividePlayers(skill1))  # Output: 22

skill2 = [3,4]
print(solution.dividePlayers(skill2))  # Output: 12

skill3 = [1,1,2,3]
print(solution.dividePlayers(skill3))  # Output: -1
