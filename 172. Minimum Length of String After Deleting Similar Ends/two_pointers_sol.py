# Minimum Length of String After Deleting Similar Ends
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
