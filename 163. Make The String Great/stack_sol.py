# Make The String Great
# Stack Solution:

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and abs(ord(s[i]) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
    
# TIme Complexity: O(n), where n is the length of the string s. We traverse the string once, performing constant-time operations (push and pop) for each character.
# Space Complexity: O(n) in the worst case, where all characters in the string are added to the stack. In the best case, the space complexity can be O(1) if all characters are removed.
# This stack-based approach efficiently handles the problem of removing adjacent characters that differ only in case, ensuring that we end up with a "good" string as defined in the problem statement.

# Test Cases:
# Test Case 1
print(Solution().makeGood('leEeetcode')) # 'leetcode'

# Test Case 2
print(Solution().makeGood('abBAcC')) # ''

# Test Case 3
print(Solution().makeGood('s')) # 's'
