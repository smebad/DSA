# Array With Elements Not Equal to Average of Neighbors
# Greedy Solution:
from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        l, r = 0, len(nums) - 1
        while len(res) != len(nums):
            res.append(nums[l])
            l += 1
            if l <= r:
                res.append(nums[r])
                r -= 1
        return res

# Time Complexity: O(n log n), where n is the length of the input array nums. This is due to the sorting step.
# Space Complexity: O(n), as we are using an additional list res to store the rearranged elements.
# This greedy solution is efficient and works well within the given constraints.


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    print("Test Case 1 Output:", solution.rearrangeArray(nums1))
    
    # Test Case 2
    nums2 = [6, 2, 0, 9, 7]
    print("Test Case 2 Output:", solution.rearrangeArray(nums2))
    
    # Additional Test Case 3
    nums3 = [10, 20, 30, 40, 50, 60]
    print("Test Case 3 Output:", solution.rearrangeArray(nums3))
    
    # Additional Test Case 4
    nums4 = [5, 3, 8, 6, 2, 7, 4, 1]
    print("Test Case 4 Output:", solution.rearrangeArray(nums4))
