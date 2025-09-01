# Count the Number of Consistent Strings
# Brute Force Solution:
from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0

        for w in words:
            flag = 1
            for c in w:
                if c not in allowed:
                    flag = 0
                    break
            res += flag

        return res

# Time Complexity: O(n * m * l), where n is the number of words, m is the maximum length of a word, and l is the length of the allowed string. In this approach, we are checking each character of each word against the allowed string, leading to the nested loop structure.
# Space Complexity: O(1) as we are using a constant amount of space regardless of the input size.
# This brute force solution is optimal for small input sizes but may not perform well for larger inputs due to its high time complexity.


# Test Cases
sol = Solution()

# Test Case 1:
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(sol.countConsistentStrings(allowed, words))  # Output: 2

# Test Case 2:
allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
print(sol.countConsistentStrings(allowed, words))  # Output: 7

# Test Case 3:
allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
print(sol.countConsistentStrings(allowed, words))  # Output: 4

