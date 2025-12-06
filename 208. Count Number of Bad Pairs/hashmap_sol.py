# Count Number of Bad Pairs
# Hash Map Solution:
from typing import List
from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        total_pairs = 0
        count = defaultdict(int)

        for i in range(len(nums)):
            total_pairs += i
            good_pairs += count[nums[i] - i]
            count[nums[i] - i] += 1

        return total_pairs - good_pairs
    
# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once.
# Space Complexity: O(n) in the worst case, where we store counts for each unique value of nums[i] - i in the hashmap.
# This hashmap solution if efficient for large input sizes due to its linear time complexity.

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [4, 1, 3, 3]
    print(solution.countBadPairs(nums1))  # Expected output: 5

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(solution.countBadPairs(nums2))  # Expected output: 0
