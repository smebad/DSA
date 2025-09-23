# Minimum Recolors to Get K Consecutive Black Blocks
# Sliding Window Solution:

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_w = 0
        for i in range(k):
            if blocks[i] == 'W':
                count_w += 1

        res = count_w
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                count_w -= 1
            if blocks[i] == 'W':
                count_w += 1
            res = min(res, count_w)
        return res
    
# Time Complexity: O(n), where n is the length of the blocks string. In this approach, we iterate through the blocks string once to initialize the count of 'W' characters in the first k-length substring, and then we slide the window across the string, updating the count in constant time for each position.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.
# This sliding window solution is more efficient than the brute force approach, especially for larger inputs, as it reduces the time complexity from O(n * k) to O(n).


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
