# Optimal Partition of String
# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

# Return the minimum number of substrings in such a partition.

# Note that each character should belong to exactly one substring in a partition.

 

# Example 1:

# Input: s = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.
# Example 2:

# Input: s = "ssssss"
# Output: 6
# Explanation:
# The only valid partition is ("s","s","s","s","s","s").
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only English lowercase letters.


# HashSet Solution:
class Solution:
    def partitionString(self, s: str) -> int:
        curSet = set()
        res = 1
        for c in s:
            if c in curSet:
                res += 1
                curSet.clear()
            curSet.add(c)
        return res

# Time Complexity: O(n), where n is the length of the string s. We traverse the string once.
# Space Complexity: O(1), since the size of the set is bounded by the number of unique characters (26 lowercase English letters).
# This hashset-based solution is efficient and straightforward for solving the problem of partitioning a string into substrings with unique characters.


# Test Cases:
sol = Solution()

# Test Case 1:
s1 = "abacaba"
print(sol.partitionString(s1))  # Expected output: 4

# Test Case 2:
s2 = "ssssss"
print(sol.partitionString(s2))  # Expected output: 6