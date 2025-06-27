# Decode String
# One Stack Solution:

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)

        return "".join(stack)
    
# Time Complexity: (n + N^2), where n is the length of the input string s. The first part, O(n), accounts for iterating through each character in s. The second part, O(N^2), arises from the repeated concatenation of substrings when building the final result, which can lead to quadratic time complexity in the worst case due to the nature of string concatenation in Python.
# Space Complexity: O(n + N^2), where n is the length of the input string s. The space complexity arises from the stack used to store characters and substrings during the decoding process, which can grow up to O(n) in size. Additionally, the final result can also take up to O(N^2) space due to the repeated concatenation of substrings.
# This solution is efficient for the given constraints, but it is important to note that the quadratic time complexity in the worst case can lead to performance issues for larger inputs. In practice, the actual performance will depend on the specific structure of the input string and how many nested brackets and repeated substrings are present.

# Test Cases
# Test Case 1:
s1 = "3[a]2[bc]"
expected1 = "aaabcbc"
result1 = Solution().decodeString(s1)
print(result1)  # Output: "aaabcbc"

# Test Case 2:
s2 = "3[a2[c]]"
expected2 = "accaccacc"
result2 = Solution().decodeString(s2)
print(result2)  # Output: "accaccacc"

# Test Case 3:
s3 = "2[abc]3[cd]ef"
expected3 = "abcabccdcdcdef"
result3 = Solution().decodeString(s3)
print(result3)  # Output: "abcabccdcdcdef"
