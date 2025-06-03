# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.


# Vertical Scanning Solution:
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
    
# Time Complexity: O(n * m), where n is the number of strings and m is the length of the longest string. This is because we iterate over the length of the longest string for each string in the list.
# Space Complexity: O(1) because we use a constant amount of space for the variables used in the function.
# This solution is optimal for large inputs as it takes O(n * m) time complexity.


# Test Cases
# Test Case 1
strs = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))  # Expected output: "fl"

# Test Case 2
strs = ["dog","racecar","car"]
solution = Solution()
print(solution.longestCommonPrefix(strs))  # Expected output: ""