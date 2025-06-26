# Simplify Path
# Stack solution:

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c

        return "/" + "/".join(stack)
    
# Time Complexity: O(n), where n is the length of the input path. This is because we iterate through each character in the path exactly once.
# Space Complexity: O(n), where n is the number of valid directory names in the simplified path. In the worst case, all directory names are valid and stored in the stack.
# The stack can grow to the size of the number of valid directory names in the path, which is why we consider it O(n) in terms of space complexity.
# This solution efficiently handles the simplification of the Unix-style file system path using a stack to manage directory names and handle special cases like current and parent directories.


# Test Cases
# Test case 1:
input1 = "/home/"
output1 = "/home"
result1 = Solution().simplifyPath(input1)
print("Test case 1:", "Passed" if result1 == output1 else f"Failed (Got {result1})")

# Test case 2:
input2 = "/home//foo/"
output2 = "/home/foo"
result2 = Solution().simplifyPath(input2)
print("Test case 2:", "Passed" if result2 == output2 else f"Failed (Got {result2})")

# Test case 3:
input3 = "/home/user/Documents/../Pictures"
output3 = "/home/user/Pictures"
result3 = Solution().simplifyPath(input3)
print("Test case 3:", "Passed" if result3 == output3 else f"Failed (Got {result3})")
