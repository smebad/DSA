# Make The String Great
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
