# Group Anagrams
# Sorting solution:
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
    
# Time complexity: O(m * nlogn), where m is the number of strings and n is the maximum length of a string. This is because we sort each string, which takes O(nlogn) time, and we do this for m strings.
# Space complexity: O(m * n), where m is the number of strings and n is the maximum length of a string. This is because we store all the strings in the result list and the dictionary.


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
