# Minimum String Length After Removing Substrings - LeetCode
# Stack Solution:
class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for c in s:
            stack.append(c)
            
            if (len(stack) >= 2 and (
                (stack[-2] == "A" and stack[-1] == "B") or
                (stack[-2] == "C" and stack[-1] == "D")
            )):
                stack.pop()
                stack.pop()

        return len(stack)

# Time Complexity: O(n), where n is the length of the string s. We traverse the string once.
# Space Complexity: O(n) in the worst case, where all characters are pushed onto the stack.
# This stack solution is efficient and straightforward for the problem at hand.


# Test Cases:
# Test Case 1:
s1 = "ABFCACDB"
sol = Solution()
print(sol.minLength(s1))  # Expected output: 2

# Test Case 2:  
s2 = "ACBBD"
print(sol.minLength(s2))  # Expected output: 5
