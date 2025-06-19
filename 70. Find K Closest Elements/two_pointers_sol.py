# Find K Closest Elements
# Two Pointers Solution:

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        
        return arr[l: r + 1]
    
# Time Complexity: O(n - k) where n is the length of the array and k is the number of closest elements to find. The two pointers traverse the array, adjusting the left and right pointers until the range contains exactly k elements.
# Space Complexity: O(k) for the output list that contains the k closest elements.
# Note: The two pointers approach efficiently narrows down the range of indices to find the k closest elements to x in the sorted array. It compares the absolute differences between the elements and x, adjusting the pointers accordingly until exactly k elements are left in the range.
# This solution is optimal for the problem and works well with the constraints provided.

# Test Cases
# Test Case 1:
arr = [1, 2, 3, 4, 5]
k = 4
x = 3
print(Solution().findClosestElements(arr, k, x))  # Output: [1, 2, 3, 4]

# Test Case 2:
arr = [1, 1, 2, 3, 4, 5]
k = 4
x = -1
print(Solution().findClosestElements(arr, k, x))  # Output: [1, 1, 2, 3]
