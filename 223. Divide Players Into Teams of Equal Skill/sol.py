# Divide Players Into Teams of Equal Skill
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

# The chemistry of a team is equal to the product of the skills of the players on that team.

# Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

 

# Example 1:

# Input: skill = [3,2,5,1,3,4]
# Output: 22
# Explanation: 
# Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
# The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
# Example 2:

# Input: skill = [3,4]
# Output: 12
# Explanation: 
# The two players form a team with a total skill of 7.
# The chemistry of the team is 3 * 4 = 12.
# Example 3:

# Input: skill = [1,1,2,3]
# Output: -1
# Explanation: 
# There is no way to divide the players into teams such that the total skill of each team is equal.
 

# Constraints:

# 2 <= skill.length <= 105
# skill.length is even.
# 1 <= skill[i] <= 1000

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