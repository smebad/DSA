# Minimum Time to Make Rope Colorful
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
