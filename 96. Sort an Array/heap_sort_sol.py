# Sort an Array
# Heap-Sort Solution:
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapSort(nums)
        return nums
    
    def heapify(self, arr, n, i):
        l = (i << 1) + 1
        r = (i << 1) + 2
        largestNode = i
        
        if l < n and arr[l] > arr[largestNode]:
            largestNode = l
        
        if r < n and arr[r] > arr[largestNode]:
            largestNode = r
        
        if largestNode != i:
            arr[i], arr[largestNode] = arr[largestNode], arr[i]
            self.heapify(arr, n, largestNode)
    
    def heapSort(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
        
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
    
# Time Complexity: O(n log n) where n is the number of elements in the array. This is because we build the heap in O(n) time and then perform n-1 heapify operations, each taking O(log n) time.
# Space Complexity: O(log n) for the recursion stack in the heapify function, which is the maximum depth of the recursion tree.
# This heap sort implementation sorts the array in-place, so it does not require additional space for another array.
# This heap sort implementation is efficient and works well for sorting arrays, especially when the array size is large.


# Test Case
# Test Case 1:
nums = [5, 2, 3, 1]
solution = Solution()
print(solution.sortArray(nums))# Output: [1, 2, 3, 5]

# Test Case 2:
nums = [5, 1, 1, 2, 0, 0]
solution = Solution()
print(solution.sortArray(nums))# Output: [0, 0, 1, 1, 2, 5]
