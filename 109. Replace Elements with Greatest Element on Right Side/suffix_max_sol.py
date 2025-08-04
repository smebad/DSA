# Replace Elements with Greatest Element on Right Side
# Suffix-Max Solution:
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans
    
# Time Complexity: O(n) where n is the length of the array. This is because we traverse the array once.
# Space Complexity: O(1) for the output array, as we are not using any additional data structures that grow with input size.
# This suffix-max approach efficiently computes the greatest element to the right of each index in a single pass, making it optimal for this problem.

# Test Cases
# Test Case 1:
arr = [17,18,5,4,6,1]
print(Solution().replaceElements(arr)) # Expected Output: [18,6,6,6,1,-1]

# Test Case 2:
arr = [400]
print(Solution().replaceElements(arr)) # Expected Output: [-1]
