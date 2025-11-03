# Repeated DNA Sequences
# Hash Set Solution:
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()

        for l in range(len(s) - 9):
            cur = s[l: l + 10]
            if cur in seen:
                res.add(cur)
            seen.add(cur)
        return list(res)
    
# Time Complexity: O(n), where n is the length of the string s. We traverse the string once to extract all 10-letter-long substrings.
# Space Complexity: O(n), in the worst case, we may store all substrings in the seen set. The res set will store only the repeated substrings, which is at most n/10 in size.
# This hash set solution is efficient and straightforward for finding repeated DNA sequences.


# Test Cases:
sol = Solution()

# Test Case 1:
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(sol.findRepeatedDnaSequences(s))  # Output: ["AAAAACCCCC", "CCCCCAAAAA"]

# Test Case 2:
s = "AAAAAAAAAAAAA"
print(sol.findRepeatedDnaSequences(s))  # Output: ["AAAAAAAAAA"]
