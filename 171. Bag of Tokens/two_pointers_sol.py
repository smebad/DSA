# Bag of Tokens
# You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] denotes the value of tokeni.

# Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):

# Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
# Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
# Return the maximum possible score you can achieve after playing any number of tokens.

 

# Example 1:

# Input: tokens = [100], power = 50

# Output: 0

# Explanation: Since your score is 0 initially, you cannot play the token face-down. You also cannot play it face-up since your power (50) is less than tokens[0] (100).

# Example 2:

# Input: tokens = [200,100], power = 150

# Output: 1

# Explanation: Play token1 (100) face-up, reducing your power to 50 and increasing your score to 1.

# There is no need to play token0, since you cannot play it face-up to add to your score. The maximum score achievable is 1.

# Example 3:

# Input: tokens = [100,200,300,400], power = 200

# Output: 2

# Explanation: Play the tokens in this order to get a score of 2:

# Play token0 (100) face-up, reducing power to 100 and increasing score to 1.
# Play token3 (400) face-down, increasing power to 500 and reducing score to 0.
# Play token1 (200) face-up, reducing power to 300 and increasing score to 1.
# Play token2 (300) face-up, reducing power to 0 and increasing score to 2.
# The maximum score achievable is 2.

 

# Constraints:

# 0 <= tokens.length <= 1000
# 0 <= tokens[i], power < 104


# Two Pointers Solution:
from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = score = 0
        tokens.sort()
        l, r = 0, len(tokens) - 1
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                score += 1
                res = max(res, score)
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
            else:
                break
        return res
    
# Time Complexity: O(n log n), where n is the number of tokens. This is due to the sorting step. The two-pointer traversal takes O(n) time.
# Space Complexity: O(1), as we are using only a constant amount of extra space.
# This two-pointer approach efficiently maximizes the score by always opting to play the smallest token face-up when possible and using the largest token face-down to regain power when necessary.


# Test Cases:
solution = Solution()

# Test Case 1
tokens1 = [100]
power1 = 50
print(solution.bagOfTokensScore(tokens1, power1))  # Output: 0

# Test Case 2
tokens2 = [200, 100]
power2 = 150
print(solution.bagOfTokensScore(tokens2, power2))  # Output: 1

# Test Case 3
tokens3 = [100, 200, 300, 400]
power3 = 200
print(solution.bagOfTokensScore(tokens3, power3))  # Output: 2