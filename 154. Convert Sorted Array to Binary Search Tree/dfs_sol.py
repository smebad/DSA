# Convert Sorted Array to Binary Search Tree
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

# Example 1:


# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:


# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.


# Depth First Search Solution:
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root

        return helper(0, len(nums) - 1)
    
# Time Complexity: O(n), where n is the number of elements in the input array. This is because we visit each element exactly once to create the tree nodes.
# Space Complexity: O(log n) for the recursion stack in the case of a balanced tree. In the worst case (unbalanced tree), the space complexity can go up to O(n).
# However, since the input array is sorted and we are always choosing the middle element as the root, the tree will be balanced, leading to a space complexity of O(log n).
# This depth first search (DFS) approach is efficient and straightforward for constructing a height-balanced binary search tree from a sorted array.


# Test Cases:
solution = Solution()

# Test Case 1:
nums1 = [-10, -3, 0, 5, 9]
result1 = solution.sortedArrayToBST(nums1)
print(result1.val)  # Expected Output: 0
print(result1.left.val)  # Expected Output: -3
print(result1.right.val)  # Expected Output: 9
print(result1.left.left.val)  # Expected Output: -10
print(result1.right.left)  # Expected Output: None
print(result1.right.right.val)  # Expected Output: 5

# Test Case 2:
nums2 = [1, 3]
result2 = solution.sortedArrayToBST(nums2)
print(result2.val)  # Expected Output: 3
print(result2.left)  # Expected Output: None
print(result2.right.val)  # Expected Output: 1