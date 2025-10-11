# Minimum Number of Swaps to Make the String Balanced
# Greedy solution:
class Solution:
    def minSwaps(self, s: str) -> int:
        stackSize = 0
        for c in s:
            if c == '[':
                stackSize += 1
            elif stackSize > 0:
                stackSize -= 1
        return (stackSize + 1) // 2

# Time complexity: O(n), where n is the length of the string s. We traverse the string once, performing constant-time operations for each character.
# Space complexity: O(1) since we are using a fixed amount of extra space (stackSize) regardless of the input size.
# This greedy solution efficiently counts the unmatched closing brackets and calculates the minimum number of swaps needed to balance the string.


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
