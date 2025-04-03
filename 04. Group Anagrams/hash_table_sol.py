# Group Anagrams
# Solved 
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.


# Hash table solution:
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    
# Time Complexity: O(m * n), where m is the number of strings and n is the maximum length of a string.
# Space Complexity: O(m * n), where m is the number of strings and n is the maximum length of a string.


# Test Cases
# Test case 1
strs = ["act","pots","tops","cat","stop","hat"]
solution = Solution()
print(solution.groupAnagrams(strs))  # Expected output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Test case 2
strs = ["x"]
solution = Solution()
print(solution.groupAnagrams(strs))  # Expected output: [["x"]]

# Test case 3
strs = [""]
solution = Solution()
print(solution.groupAnagrams(strs))  # Expected output: [[""]]