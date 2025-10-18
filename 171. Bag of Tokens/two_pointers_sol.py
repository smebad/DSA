# Bag of Tokens
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
