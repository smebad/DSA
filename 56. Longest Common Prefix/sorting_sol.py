# Longest Common Prefix
# Sorting Solution:

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        strs = sorted(strs)
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]
    
# Time Complexity: O(n*mlogm), where n is the number of strings and m is the length of the longest string. This is because we sort the strings, which takes O(n*mlogm). It is also because we iterate over the length of the longest string for each string in the list.
# Space Complexity: O(1) because we use a constant amount of space for the variables used in the function.
# This solution is optimal for large inputs as it takes O(n*mlogm) time complexity.


# Test Cases
# Test Case 1
strs = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))  # Expected output: "fl"

# Test Case 2
strs = ["dog","racecar","car"]
solution = Solution()
print(solution.longestCommonPrefix(strs))  # Expected output: ""
