# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Sliding Window Solution:
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k - 1])

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]
            if (curSum / k) >= threshold:
                res += 1
            curSum -= arr[L]
        return res
    
# Time Complexity: O(n), where n is the length of the array arr. We traverse the array once.
# Space Complexity: O(1), as we use a constant amount of extra space regardless of the input size.
# This solution is efficient and works well within the given constraints.


# Test Cases:
# Test Case 1:
arr1 = [2, 2, 2, 2, 5, 5, 5, 8]
k1 = 3
threshold1 = 4
print(Solution().numOfSubarrays(arr1, k1, threshold1))  # Output: 3

# Test Case 2:
arr2 = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
k2 = 3
threshold2 = 5
print(Solution().numOfSubarrays(arr2, k2, threshold2))  # Output: 6
