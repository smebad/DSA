# Subtree of Another Tree
# Depth First Search (DFS) solution:

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or 
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                   self.sameTree(root.right, subRoot.right))
        return False
    

# Time Complexity: O(m * n) where m is the number of nodes in the root tree and n is the number of nodes in the subRoot tree. In the worst case, we may have to check every node in the root tree against every node in the subRoot tree. This is because for each node in the root tree, we may have to traverse the entire subRoot tree to check if it is a subtree.
# Space Complexity: O(m + n) where m is the number of nodes in the root tree and n is the number of nodes in the subRoot tree. This is because we are using recursion to traverse both trees, which can take up to O(m + n) space on the call stack in the worst case. In addition, we are also using O(m + n) space to store the nodes in both trees.
# This DFS solution is efficient and works well for the given problem. It checks if the subRoot tree is a subtree of the root tree by recursively checking if the two trees are the same at each node. If they are, it returns True, otherwise it continues to check the left and right subtrees of the root tree. The time and space complexity of this solution is acceptable for the given constraints.


# Test cases:

# Test Case 1:
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(Solution().isSubtree(root, subRoot)) # True

# Test Case 2:
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(0)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(Solution().isSubtree(root, subRoot)) # False
