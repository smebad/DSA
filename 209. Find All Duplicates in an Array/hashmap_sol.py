# Find All Duplicates in an Array
# Hashmap Solution:
from typing import List
from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for num in count:
            if count[num] == 2:
                res.append(num)

        return res
    
# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once to build the count dictionary and once more to collect duplicates.
# Space Complexity: O(n) in the worst case, where all elements are unique and we store them in the count dictionary.
# This hashmap solution is straightforward but uses extra space compared to the negative marking solution.


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [4,3,2,7,8,2,3,1]
    print(solution.findDuplicates(nums1))  # Expected output: [2, 3]

    # Test Case 2
    nums2 = [1,1,2]
    print(solution.findDuplicates(nums2))  # Expected output: [1]

    # Test Case 3
    nums3 = [1]
    print(solution.findDuplicates(nums3))  # Expected output: []
