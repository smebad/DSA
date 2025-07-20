# Sort an Array
# Merge Sort Solution:
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L : M + 1], arr[M + 1 : R + 1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1
        
        def mergeSort(arr, l, r):
            if l == r:
                return

            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return
        
        mergeSort(nums, 0, len(nums))
        return nums
    
# Time Complexity: O(n log n) where n is the number of elements in the array. This is because we are dividing the array into halves recursively and merging them back.
# Space Complexity: O(n) for the temporary arrays used during the merge process. This is the space used to store the left and right halves of the array during merging.
# This merge sort implementation is efficient and works well for sorting arrays, especially when the array size is large.


# Test Case
# Test Case 1:
nums = [5, 2, 3, 1]
solution = Solution()
print(solution.sortArray(nums))# Output: [1, 2, 3, 5]

# Test Case 2:
nums = [5, 1, 1, 2, 0, 0]
solution = Solution()
print(solution.sortArray(nums))# Output: [0, 0, 1, 1, 2, 5]
