# Get Equal Substrings Within Budget
# Sliding Window solution:

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curCost = 0
        l = 0
        res = 0

        for r in range(len(s)):
            curCost += abs(ord(s[r]) - ord(t[r]))
            while curCost > maxCost:
                curCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            res = max(res, r - l + 1)

        return res

# Time complexity: O(n), where n is the length of the input strings s and t. We traverse the strings once with the right pointer, and the left pointer also moves at most n times in total. Thus, the overall time complexity is linear.
# Space complexity: O(1), as we are using a constant amount of extra space for variables (curCost, l, r, res) regardless of the input size.
# This sliding window approach is efficient and works well within the given constraints.


# Test Cases
sol = Solution()

# Test Case 1:
s = "abcd"
t = "bcdf"
maxCost = 3
print(sol.equalSubstring(s, t, maxCost))  # Output: 3

# Test Case 2:
s = "abcd"
t = "cdef"
maxCost = 3
print(sol.equalSubstring(s, t, maxCost))  # Output: 1

# Test Case 3:
s = "abcd"
t = "acde"
maxCost = 0
print(sol.equalSubstring(s, t, maxCost))  # Output: 1
