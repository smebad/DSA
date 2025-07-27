# Maximum Difference Between Even and Odd Frequency I
# Counting Solution:
from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        oddMax, evenMin = 0, len(s) 

        for cnt in count.values():
            if cnt & 1:
                oddMax = max(oddMax, cnt)
            else:
                evenMin = min(evenMin, cnt)

        return oddMax - evenMin
    
# Time Complexity: O(n), where n is the length of the string s. This is because we are iterating through the string once and performing constant time operations for each character.
# Space Complexity: O(1), since the frequency count will have a maximum of 26 entries (for each lowercase letter).
# This counting solution efficiently calculates the maximum difference between the frequencies of characters with odd and even counts.
    
# Test Case
solution = Solution()
# Test Case 1:
s = "aaaaabbc"
print(solution.maxDifference(s))  # Output: 3

# Test Case 2:
s = "abcabcab"
print(solution.maxDifference(s))  # Output: 1
