# Minimum Add to Make Parentheses Valid
# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

 

# Example 1:

# Input: s = "())"
# Output: 1
# Example 2:

# Input: s = "((("
# Output: 3
 

# Constraints:

# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.


# Solution:
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_cnt = 0
        res = 0

        for c in s:
            if c == "(":
                open_cnt += 1
            else:
                if open_cnt > 0:
                    res += 1
                open_cnt = max(open_cnt - 1, 0)

        return res + open_cnt
    
# Time Complexity: O(n), where n is the length of the string s. We traverse the string once.
# Space Complexity: O(1), we use a constant amount of extra space.
# This solution is efficient and works well within the given constraints.


# Test Cases:
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    s1 = "())"
    print(sol.minAddToMakeValid(s1))  # Expected output: 1

    # Test Case 2
    s2 = "((("
    print(sol.minAddToMakeValid(s2))  # Expected output: 3