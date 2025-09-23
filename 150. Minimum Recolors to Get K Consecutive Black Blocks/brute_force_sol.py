# Minimum Recolors to Get K Consecutive Black Blocks
# Brute Force Solution:

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = len(blocks)
        for i in range(len(blocks) - k + 1):
            count_w = 0
            for j in range(i, i + k):
                if blocks[j] == 'W':
                    count_w += 1
            res = min(res, count_w)
        return res
    
# Time Complexity: O(n * k), where n is the length of the blocks string and k is the number of consecutive black blocks desired. In this approach, we iterate through all possible starting indices for k-length substrings (which takes O(n) time), and for each substring, we count the number of 'W' characters (which takes O(k) time).
# Space Complexity: O(1), as we are using a constant amount of extra space regardless
# This brute force solution may not be efficient for large inputs, but it is straightforward and easy to understand.


# Test Cases:
solution = Solution()

# Test Case 1
blocks = "WBBWWBBWBW"
k = 7
print(solution.minimumRecolors(blocks, k)) # Output: 3

# Test Case 2
blocks = "WBWBBBW"
k = 2
print(solution.minimumRecolors(blocks, k)) # Output: 0
