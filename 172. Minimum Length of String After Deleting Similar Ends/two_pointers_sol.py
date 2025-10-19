# Minimum Length of String After Deleting Similar Ends
# Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

# Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
# Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
# The prefix and the suffix should not intersect at any index.
# The characters from the prefix and suffix must be the same.
# Delete both the prefix and the suffix.
# Return the minimum length of s after performing the above operation any number of times (possibly zero times).

 

# Example 1:

# Input: s = "ca"
# Output: 2
# Explanation: You can't remove any characters, so the string stays as is.
# Example 2:

# Input: s = "cabaabac"
# Output: 0
# Explanation: An optimal sequence of operations is:
# - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
# - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
# - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
# - Take prefix = "a" and suffix = "a" and remove them, s = "".
# Example 3:

# Input: s = "aabccabba"
# Output: 3
# Explanation: An optimal sequence of operations is:
# - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
# - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
 

# Constraints:

# 1 <= s.length <= 105
# s only consists of characters 'a', 'b', and 'c'.


# Two Pointers Solution:
class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1

        while l < r and s[l] == s[r]:
            tmp = s[l]
            while l <= r and s[l] == tmp:
                l += 1
            while l <= r and s[r] == tmp:
                r -= 1
        return r - l + 1
    
# Time Complexity: O(n), where n is the length of the string s. In the worst case, we may need to traverse the entire string once.
# Space Complexity: O(1), as we are using only a constant amount of extra space.
# This two-pointers solution is efficient and works well within the given constraints. It effectively reduces the string by removing matching prefixes and suffixes until no more valid operations can be performed.


# Test Cases:
# Test Case 1
print(Solution().minimumLength('ca')) # 2

# Test Case 2
print(Solution().minimumLength('cabaabac')) # 0

# Test Case 3
print(Solution().minimumLength('aabccabba')) # 3