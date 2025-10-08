# Make The String Great
# Given a string s of lower and upper case English letters.

# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

# Notice that an empty string is also good.

 

# Example 1:

# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
# Example 2:

# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same answer. For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""
# Example 3:

# Input: s = "s"
# Output: "s"
 

# Constraints:

# 1 <= s.length <= 100
# s contains only lower and upper case English letters.


# Two-pointers Solution:
class Solution:
    def makeGood(self, s: str) -> str:
        l = 0
        s = list(s)
        for r in range(len(s)):
            if l > 0 and abs(ord(s[r]) - ord(s[l - 1])) == 32:
                l -= 1
            else:
                s[l] = s[r]
                l += 1
        return ''.join(s[:l])
    
# Time Complexity: O(n), where n is the length of the string s. We traverse the string once, performing constant-time operations for each character.
# Space Complexity: O(n) in the worst case, where all characters in the string are retained. However, since we are modifying the string in place (using a list), the additional space used is O(1) for the pointer variables.
# This two-pointer approach efficiently handles the problem of removing adjacent characters that differ only in case, ensuring that we end up with a "good" string as defined in the problem statement.    

# Test Cases:
# Test Case 1
print(Solution().makeGood('leEeetcode')) # 'leetcode'

# Test Case 2
print(Solution().makeGood('abBAcC')) # ''

# Test Case 3
print(Solution().makeGood('s')) # 's'