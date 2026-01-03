# Minimum Time to Make Rope Colorful
# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

# Return the minimum time Bob needs to make the rope colorful.

 

# Example 1:


# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3
# Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
# Bob can remove the blue balloon at index 2. This takes 3 seconds.
# There are no longer two consecutive balloons of the same color. Total time = 3.
# Example 2:


# Input: colors = "abc", neededTime = [1,2,3]
# Output: 0
# Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.
# Example 3:


# Input: colors = "aabaa", neededTime = [1,2,3,4,1]
# Output: 2
# Explanation: Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
# There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
 

# Constraints:

# n == colors.length == neededTime.length
# 1 <= n <= 105
# 1 <= neededTime[i] <= 104
# colors contains only lowercase English letters.


# Two Pointer Solution:
from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l, res = 0, 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
            else:
                l = r
        return res

# Time Complexity: O(n), where n is the length of the colors string. We traverse the string once.
# Space Complexity: O(1), as we use only a constant amount of extra space.
# This solution efficiently calculates the minimum time required to make the rope colorful by using a two-pointer technique to track consecutive balloons of the same color and summing the removal times of the less costly balloons.


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    colors = "abaac"
    neededTime = [1,2,3,4,5]
    print(solution.minCost(colors, neededTime))  # Expected output: 3

    # Test Case 2
    colors = "abc"
    neededTime = [1,2,3]
    print(solution.minCost(colors, neededTime))  # Expected output: 0

    # Test Case 3
    colors = "aabaa"
    neededTime = [1,2,3,4,1]
    print(solution.minCost(colors, neededTime))  # Expected output: 2