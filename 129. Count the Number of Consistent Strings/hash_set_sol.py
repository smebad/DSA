# Count the Number of Consistent Strings
# Hash-Set Solution:
from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)

        res = len(words)
        for w in words:
            for c in w:
                if c not in allowed:
                    res -= 1
                    break

        return res

# Time Complexity: O(n * l + m), where n is the number of words, l is the maximum length of a word, and m is the length of the allowed string. The first part accounts for the time taken to check each character of each word against the allowed set, and the second part accounts for the time taken to create the allowed set.
# Space Complexity: O(m) where m is the length of the allowed string, as we are storing the allowed characters in a set.
# This hash set approach is more efficient than the brute force method, especially for larger inputs.

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

