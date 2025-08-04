# Replace Elements with Greatest Element on Right Side
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

 

# Example 1:

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
# Example 2:

# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.
 

# Constraints:

# 1 <= arr.length <= 104
# 1 <= arr[i] <= 105


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