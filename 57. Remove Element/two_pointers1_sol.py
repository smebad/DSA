# Remove Element
# Two Pointers (1) solution:

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    

# Time complexity: O(n) where n is the length of nums and the number of elements in nums which are not equal to val. This is due to the for loop which iterates over the length of nums.
# Space complexity: O(1) where 1 is the number of elements in nums which are not equal to val. This is due to the k variable which stores the number of elements in nums which are not equal to val.
# This two pointer solution is efficient and works well for the problem.


# Test cases
# Test Case 1:
nums = [3,2,2,3]
val = 3
print(Solution().removeElement(nums, val))  # Output: 2

# Test Case 2:
nums = [0,1,2,2,3,0,4,2]
val = 2
print(Solution().removeElement(nums, val))  # Output: 5
