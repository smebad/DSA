# Kth Distinct String in an Array
# Hash-Map Solution:
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}

        for s in arr:
            if s not in count:
                count[s] = 0
            count[s] += 1

        for s in arr:
            if count[s] == 1:
                k -= 1
                if k == 0:
                    return s

        return ""

# Time Complexity: O(n), where n is the length of the input array. We use a single pass to count occurrences and another pass to find the k-th distinct string.
# Space Complexity: O(n), for storing the count of each string in the hash map.
# This hash-map solution is more efficient than the brute-force approach, especially for larger input sizes.

# Test Cases
# Test Case 1:
arr1 = ["d", "b", "c", "b", "c", "a"]
k1 = 2
print(Solution().kthDistinct(arr1, k1))  # Output: "a"

# Test Case 2:
arr2 = ["aaa", "aa", "a"]
k2 = 1
print(Solution().kthDistinct(arr2, k2))  # Output: "aaa"

# Test Case 3:
arr3 = ["a", "b", "a"]
k3 = 3

print(Solution().kthDistinct(arr3, k3))  # Output: ""
