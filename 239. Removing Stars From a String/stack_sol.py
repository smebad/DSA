# Removing Stars From a String
# Stack Solution:
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                stack and stack.pop()
            else:
                stack.append(c)
        return "".join(stack)

# Time Complexity: O(n), where n is the length of the string s.We traverse the string once, performing constant-time operations (push/pop) for each character.
# Space Complexity: O(n) in the worst case, where all characters in s are non-star characters, and we store them all in the stack.
# This stack-based solution is efficient and straightforward for the problem at hand.


# Test Cases:
s1 = "leet**cod*e"
sol = Solution()
print(sol.removeStars(s1))  # Expected output: "lecoe"

s2 = "erase*****"
print(sol.removeStars(s2))  # Expected output: ""
