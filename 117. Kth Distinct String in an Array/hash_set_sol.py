# Kth Distinct String in an Array
# Hash-Set Solution:
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct, seen = set(), set()

        for s in arr:
            if s in distinct:
                distinct.remove(s)
                seen.add(s)
            elif s not in seen:
                distinct.add(s)

        for s in arr:
            if s in distinct:
                k -= 1
                if k == 0:
                    return s

        return ""

# Time Complexity: O(n), where n is the length of the input array. We use a single pass to identify distinct strings and another pass to find the k-th distinct string.
# Space Complexity: O(n), for storing the distinct strings and seen strings in hash sets.
# This hash-set solution is efficient and works well for larger input sizes.

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
