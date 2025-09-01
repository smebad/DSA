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
