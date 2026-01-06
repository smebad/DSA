# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 

# Example 1:

# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
# Example 2:

# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
 

# Constraints:

# 1 <= arr.length <= 105
# 1 <= arr[i] <= 104
# 1 <= k <= arr.length
# 0 <= threshold <= 104


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