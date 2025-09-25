# Sort Array by Increasing Frequency
# Custom Sort Solution:
from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        nums.sort(key=lambda n: (count[n], -n))
        return nums
    
# Time Complexity: O(n log n), where n is the number of elements in the array. This is due to the sorting step. The time complexity is dominated by the sorting operation, which takes O(n log n) time in the worst case.
# Space Complexity: O(n), where n is the number of unique elements in the array. This space is used by the Counter to store the frequency of each element.
# This custom sort solution is efficient and leverages Python's built-in sorting capabilities with a custom key function to achieve the desired ordering based on frequency and value.


# Test cases:
sol = Solution()

# Test Case 1:
nums1 = [1,1,2,2,2,3]
expected1 = [3,1,1,2,2,2]
print(sol.frequencySort(nums1))  # Output: [3,1,1,2,2,2]

# Test Case 2:
nums2 = [2,3,1,3,2]
expected2 = [1,3,3,2,2]
print(sol.frequencySort(nums2))  # Output: [1,3,3,2,2]

# Test Case 3:
nums3 = [-1,1,-6,4,5,-6,1,4,1]
expected3 = [5,-1,4,4,-6,-6,1,1,1]
print(sol.frequencySort(nums3))  # Output: [5,-1,4,4,-6,-6,1,1,1]
