# Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"
 

# Constraints:

# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.

# Two Pointers Solution:
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        l = 0
        for r in range(len(s)):
            if s[r] == " " or r == len(s) - 1:
                temp_l, temp_r = l, r - 1 if s[r] == " " else r
                while temp_l < temp_r:
                    s[temp_l], s[temp_r] = s[temp_r], s[temp_l]
                    temp_l += 1
                    temp_r -= 1
                l = r + 1
        return "".join(s)
    
# Time Complexity: O(n), where n is the length of the string s. We traverse the string once to reverse each word.
# Space Complexity: O(n) for converting the string to a list of characters. The in place reversal uses O(1) additional space.
# This solution is efficient and works well within the given constraints.


# Test Cases:
solution = Solution()
# Test Case 1:
s1 = "Let's take LeetCode contest"
print(solution.reverseWords(s1))  # Output: "s'teL ekat edoCteeL tsetnoc"

# Test Case 2:
s2 = "Mr Ding"
print(solution.reverseWords(s2))  # Output: "rM gniD"

# Test Case 3:
s3 = "My name is Ebad"
print(solution.reverseWords(s3))  # Output: "yM eman si dabe"