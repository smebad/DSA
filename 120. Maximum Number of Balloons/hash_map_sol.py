# Maximum Number of Balloons
# Hash-Map Solution:
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        return res
    
# Time Complexity: O(n), where n is the length of the input string text. Because we traverse the string to count characters and then check against the balloon counts.
# Space Complexity: O(1), since the size of the balloon character set is constant (only 7 unique characters).
# This hash-map based approach is efficient and works well within the problem constraints.


# Test Cases
# Test Case 1:
text1 = "nlaebolko"
sol = Solution()
print(sol.maxNumberOfBalloons(text1))  # Output: 1

# Test Case 2:
text2 = "loonbalxballpoon"
print(sol.maxNumberOfBalloons(text2))  # Output: 2

# Test Case 3:
text3 = "leetcode"
print(sol.maxNumberOfBalloons(text3))  # Output: 0
