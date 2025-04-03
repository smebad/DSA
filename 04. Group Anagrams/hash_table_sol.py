# Group Anagrams
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
