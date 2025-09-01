# Count the Number of Consistent Strings
# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.

 

# Example 1:

# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
# Example 2:

# Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# Explanation: All strings are consistent.
# Example 3:

# Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 

# Constraints:

# 1 <= words.length <= 104
# 1 <= allowed.length <= 26
# 1 <= words[i].length <= 10
# The characters in allowed are distinct.
# words[i] and allowed contain only lowercase English letters.


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
