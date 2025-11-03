# Repeated DNA Sequences
# Hash Map Solution:
from typing import List
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        mp = defaultdict(int)
        res = []
        for l in range(len(s) - 9):
            cur = s[l: l + 10]
            mp[cur] += 1
            if mp[cur] == 2:
                res.append(cur)

        return res


# Test Cases:
sol = Solution()

# Test Case 1:
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(sol.findRepeatedDnaSequences(s))  # Output: ["AAAAACCCCC", "CCCCCAAAAA"]

# Test Case 2:
s = "AAAAAAAAAAAAA"
print(sol.findRepeatedDnaSequences(s))  # Output: ["AAAAAAAAAA"]
