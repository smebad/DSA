# Remove Element
Brute force solution for the problem
# Brute Force solution:
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        tmp = []
        for num in nums:
            if num == val:
                continue
            tmp.append(num)
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)
    

# Time complexity: O(n) where n is the length of nums. This is due to the for loop which iterates over the length of nums.
# Space complexity: O(n) where n is the length of nums. This is due to the tmp variable which stores the elements in nums which are not equal to val.
# This brute force solution is not efficient because it uses additional space to store the elements in nums which are not equal to val.
# However, it works well for the problem. 


# Test cases
# Test Case 1:
nums = [3,2,2,3]
val = 3
print(Solution().removeElement(nums, val))  # Output: 2

# Test Case 2:
nums = [0,1,2,2,3,0,4,2]
val = 2
print(Solution().removeElement(nums, val))  # Output: 5
