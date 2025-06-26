# Simplify Path
# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

# The rules of a Unix-style file system are as follows:

# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:

# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.

 

# Example 1:

# Input: path = "/home/"

# Output: "/home"

# Explanation:

# The trailing slash should be removed.

# Example 2:

# Input: path = "/home//foo/"

# Output: "/home/foo"

# Explanation:

# Multiple consecutive slashes are replaced by a single one.

# Example 3:

# Input: path = "/home/user/Documents/../Pictures"

# Output: "/home/user/Pictures"

# Explanation:

# A double period ".." refers to the directory up a level (the parent directory).

# Example 4:

# Input: path = "/../"

# Output: "/"

# Explanation:

# Going one level up from the root directory is not possible.

# Example 5:

# Input: path = "/.../a/../b/c/../d/./"

# Output: "/.../b/d"

# Explanation:

# "..." is a valid name for a directory in this problem.

 

# Constraints:

# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.


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
