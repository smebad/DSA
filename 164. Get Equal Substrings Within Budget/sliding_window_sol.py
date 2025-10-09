# Get Equal Substrings Within Budget
# You are given two strings s and t of the same length and an integer maxCost.

# You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

 

# Example 1:

# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# Explanation: "abc" of s can change to "bcd".
# That costs 3, so the maximum length is 3.
# Example 2:

# Input: s = "abcd", t = "cdef", maxCost = 3
# Output: 1
# Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.
# Example 3:

# Input: s = "abcd", t = "acde", maxCost = 0
# Output: 1
# Explanation: You cannot make any change, so the maximum length is 1.
 

# Constraints:

# 1 <= s.length <= 105
# t.length == s.length
# 0 <= maxCost <= 106
# s and t consist of only lowercase English letters.


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