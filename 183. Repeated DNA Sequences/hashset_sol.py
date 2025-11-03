# Repeated DNA Sequences
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either 'A', 'C', 'G', or 'T'.

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