# Optimal Partition of String
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
