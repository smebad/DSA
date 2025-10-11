# Minimum Number of Swaps to Make the String Balanced
# Stack solution:
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '[':
                stack.append(c)
            elif stack:
                stack.pop()
        return (len(stack) + 1) // 2
    
# Time complexity: O(n), where n is the length of the string s. We traverse the string once, performing constant-time operations (push and pop) for each character.
# Space complexity: O(n) in the worst case, where all characters in the string are closing brackets. In this case, the stack will store all n/2 closing brackets, leading to O(n) space usage. However, since the number of opening and closing brackets are equal, the maximum size of the stack will be n/2, which is still O(n) in terms of asymptotic complexity.
# This solution efficiently counts the unmatched closing brackets and calculates the minimum number of swaps needed to balance the string.


# Test Cases:
sol = Solution()

# Test Case 1
s1 = "][]["
print(sol.minSwaps(s1))  # Expected output: 1

# Test Case 2
s2 = "]]][["
print(sol.minSwaps(s2))  # Expected output: 2

# Test Case 3
s3 = "[]"
print(sol.minSwaps(s3))  # Expected output: 0
