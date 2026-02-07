# Maximum Number of Removable Characters
# Binary Search Solution:
from typing import List
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubseq(s, subseq, removed):
            i1 = i2 = 0
            while i1 < len(s) and i2 < len(subseq):
                if i1 in removed or s[i1] != subseq[i2]:
                    i1 += 1
                    continue
                i1 += 1
                i2 += 1
            return i2 == len(subseq)

        res = 0
        l, r = 0, len(removable) - 1
        while l <= r:
            m = (l + r) // 2
            removed = set(removable[:m + 1])
            if isSubseq(s, p, removed):
                res = max(res, m + 1)
                l = m + 1
            else:
                r = m - 1

        return res

# Time Complexity: O((n + m) * log k), where n is the length of s, m is the length of p, and k is the length of removable. The binary search runs in O(log k) and the isSubseq function runs in O(n + m) time.
# Space Complexity: O(k), where k is the length of removable, due to the set of removed indices.
# This solution is efficient for large inputs and is a common approach to problems that require checking a condition after a certain number of modifications.


# Test Cases
# Test Case 1:
s = "abcacb"
p = "ab"
removable = [3, 1, 0]
solution = Solution()
print(solution.maximumRemovals(s, p, removable))  # Output: 2

# Test Case 2:
s = "abcbddddd"
p = "abcd"
removable = [3, 2, 1, 4, 5, 6]
print(solution.maximumRemovals(s, p, removable))  # Output: 1

# Test Case 3:
s = "abcab"
p = "abc"
removable = [0, 1, 2, 3, 4]
print(solution.maximumRemovals(s, p, removable))  # Output: 0
