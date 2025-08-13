# Kth Distinct String in an Array
# A distinct string is a string that is present only once in an array.

# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

# Note that the strings are considered in the order in which they appear in the array.

 

# Example 1:

# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"
# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2, "a" is returned. 
# Example 2:

# Input: arr = ["aaa","aa","a"], k = 1
# Output: "aaa"
# Explanation:
# All strings in arr are distinct, so the 1st string "aaa" is returned.
# Example 3:

# Input: arr = ["a","b","a"], k = 3
# Output: ""
# Explanation:
# The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
 

# Constraints:

# 1 <= k <= arr.length <= 1000
# 1 <= arr[i].length <= 5
# arr[i] consists of lowercase English letters.


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