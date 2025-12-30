# Apply Operations to an Array
# Two Pointers Solution:
from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        l = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1

        return nums

# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array twice: once for applying the operations and once for shifting the zeros.
# Space Complexity: O(1), since we are modifying the input array in place and not using any additional data structures that grow with input size.
# This solution is efficient and works well within the given constraints.


# Test Cases:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [1, 2, 2, 1, 1, 0]
    print(solution.applyOperations(nums1))  # Expected Output: [1, 4, 2, 0, 0, 0]

    # Test Case 2
    nums2 = [0, 1]
    print(solution.applyOperations(nums2))  # Expected Output: [1, 0]

    # Test Case 3
    nums3 = [2, 2, 2, 2]
    print(solution.applyOperations(nums3))  # Expected Output: [4, 4, 0, 0]

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    print(solution.applyOperations(nums4))  # Expected Output: [2, 2, 1, 0, 0]

    # Test Case 5
    nums5 = [0, 0, 0]
    print(solution.applyOperations(nums5))  # Expected Output: [0, 0, 0]
