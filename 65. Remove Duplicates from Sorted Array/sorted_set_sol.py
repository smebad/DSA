# Remove Duplicates from Sorted Array
# Sorted Set Solution:

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)
    
# Time Complexity: O(n log n) where n is the length of the input array nums. Log n is the time it takes to sort the array, and n is the time it takes to iterate through the array to remove duplicates.
# Space Complexity: O(n) where n is the length of the input array nums. This is because we need to store the unique elements in a sorted set.
# This sorted set solution is not efficient for large inputs as it has a time complexity of O(n log n). It is not optimal but works well for the problem.


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

