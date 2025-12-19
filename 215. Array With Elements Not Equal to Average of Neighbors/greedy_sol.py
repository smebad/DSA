# Array With Elements Not Equal to Average of Neighbors
# You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

# More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

# Return any rearrangement of nums that meets the requirements.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: [1,2,4,5,3]
# Explanation:
# When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
# When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
# When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.
# Example 2:

# Input: nums = [6,2,0,9,7]
# Output: [9,7,6,2,0]
# Explanation:
# When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5.
# When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5.
# When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3.
# Note that the original array [6,2,0,9,7] also satisfies the conditions.
 

# Constraints:

# 3 <= nums.length <= 105
# 0 <= nums[i] <= 105


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