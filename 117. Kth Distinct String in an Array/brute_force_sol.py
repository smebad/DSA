# Kth Distinct String in an Array
# Brute-Force Solution:
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for i in range(len(arr)):
            flag = True
            for j in range(len(arr)):
                if i == j:
                    continue

                if arr[i] == arr[j]:
                    flag = False
                    break

            if flag:
                k -= 1
                if k == 0:
                    return arr[i]
        return ""

# Time Complexity: O(n^2), where n is the length of the input array. We use a nested loop to check each string against all others.
# Space Complexity: O(1), since we are using only a constant amount of extra space.
# This brute force solution is not optimal for large input sizes.

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
