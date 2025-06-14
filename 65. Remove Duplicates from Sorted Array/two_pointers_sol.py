# Remove Duplicates from Sorted Array
# Two Pointers Solution:

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
    
# Time Complexity: O(n) where n is the length of the input array nums. This is because we need to iterate through the array once to remove duplicates.
# Space Complexity: O(1) since we are not using any additional data structures.
# This two pointers solution is efficient for large inputs as it has a time complexity of O(n). It is optimal and works well for the problem.


# Test Cases:
# Test Case 1:
nums = [1,1,2]
print(Solution().removeDuplicates(nums)) # Expected Output: 2

# Test Case 2:
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums)) # Expected Output: 5

# Test Case 3:
nums = [1,2,3,4,5]
print(Solution().removeDuplicates(nums)) # Expected Output: 5

