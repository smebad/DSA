# Merge Sorted Array
# Three Pointers without extra space solution:

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        # Merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # Fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

# Time Complexity: O(m + n) where m and n are the lengths of the two arrays. This is because we are iterating over the two arrays once each.
# Space Complexity: O(1) since we are modifying the input array nums1 in-place. No additional data structures are used.
# This three pointers solution is a good solution for small inputs as it takes O(m + n) time complexity.

# Test Cases:
# Test Case 1:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)  # Expected Output: [1, 2, 2, 3, 5, 6]

# Test Case 2:
nums1 = [1]
m = 1
nums2 = []
n = 0
Solution().merge(nums1, m, nums2, n)
print(nums1)  # Expected Output: [1]

# Test Case 3:
nums1 = [0]
m = 0
nums2 = [1]
n = 1
Solution().merge(nums1, m, nums2, n)
print(nums1)  # Expected Output: [1]

