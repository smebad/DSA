# Number of Substrings Containing All Three Characters
# Sliding Window Solution:
from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        res = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1

            while len(count) == 3:
                res += len(s) - r
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l])
                l += 1

        return res

# Time Complexity: O(n), where n is the length of the string s. Each character is processed at most twice (once by the right pointer and once by the left pointer).
# Space Complexity: O(1), since the count dictionary will hold at most three key-value pairs (for 'a', 'b', and 'c').
# This sliding window approach efficiently counts the number of substrings containing all three characters by expanding and contracting the window as needed.


# Test Cases:
solution = Solution()

# Test Case 1
s = "abcabc"
print(solution.numberOfSubstrings(s))  # Output: 10

# Test Case 2
s = "aaacb"
print(solution.numberOfSubstrings(s))  # Output: 3

# Test Case 3
s = "abc"
print(solution.numberOfSubstrings(s))  # Output: 1
