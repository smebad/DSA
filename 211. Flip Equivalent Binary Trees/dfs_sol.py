# Flip Equivalent Binary Trees
# Depth-First Search Solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val != root2.val:
            return False

        return (
                self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left)
            )
    
# Time Complexity: O(n), where n is the number of nodes in the trees. In the worst case, we may need to visit all nodes in both trees.
# Space Complexity: O(h), where h is the height of the trees. This space is used by the recursion stack. In the worst case, the height of the tree can be n (for a skewed tree), leading to O(n) space complexity.
# This depth-first search solution effectively checks all possible configurations of the two trees to determine if they are flip equivalent.


# Test cases
if __name__ == "__main__":
    # Test Case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(8)

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(6)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(5)
    root2.right.right.left = TreeNode(8)
    root2.right.right.right = TreeNode(7)

    solution = Solution()
    print(solution.flipEquiv(root1, root2))  # Output: True

    # Test Case 2
    print(solution.flipEquiv(None, None))  # Output: True

    # Test Case 3
    print(solution.flipEquiv(None, TreeNode(1)))  # Output: False
