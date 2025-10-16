# Construct String from Binary Tree
# Depth-First Search solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(root):
            if not root:
                return
            res.append("(")
            res.append(str(root.val))
            if not root.left and root.right:
                res.append("()")
            preorder(root.left)
            preorder(root.right)
            res.append(")")

        preorder(root)
        return "".join(res)[1:-1]
    
# Time Complexity: O(n), where n is the number of nodes in the binary tree. We visit each node exactly once during the preorder traversal.
# Space Complexity: O(n), where n is the number of nodes in the binary tree. In the worst case, the recursion stack can go as deep as the height of the tree, which can be O(n) for a skewed tree. The result list also takes O(n) space to store the string representation.
# This depth-first search solution effectively constructs the string representation of the binary tree while adhering to the specified formatting rules.


# Test Cases:
solution = Solution()

# Test Case 1:
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
print(solution.tree2str(root1))  # Output: "1(2(4))(3)"

# Test Case 2:
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.right.right = TreeNode(4)
print(solution.tree2str(root2))  # Output: "1(2())(3(4()))"
