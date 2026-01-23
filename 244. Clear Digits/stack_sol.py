# Clear Digits
# You are given a string s.

# Your task is to remove all digits by doing this operation repeatedly:

# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.

# Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.

 

# Example 1:

# Input: s = "abc"

# Output: "abc"

# Explanation:

# There is no digit in the string.

# Example 2:

# Input: s = "cb34"

# Output: ""

# Explanation:

# First, we apply the operation on s[2], and s becomes "c4".

# Then we apply the operation on s[1], and s becomes "".

 

# Constraints:

# 1 <= s.length <= 100
# s consists only of lowercase English letters and digits.
# The input is generated such that it is possible to delete all digits.


# Stack Solution:
class Solution:
    def clearDigits(self, s: str) -> str:
        res = []

        def isdigit(c):
            return ord("0") <= ord(c) <= ord("9")
        
        for i in range(len(s)):
            if isdigit(s[i]):
                res.pop()
            else:
                res.append(s[i])

        return "".join(res)

# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(n) in the worst case, when there are no digits in the string s.
# This stack base solution is efficient for the given constraints.


# Test Cases:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    s1 = "abc"
    print(solution.clearDigits(s1))  # Expected Output: "abc"

    # Test Case 2
    s2 = "cb34"
    print(solution.clearDigits(s2))  # Expected Output: ""
