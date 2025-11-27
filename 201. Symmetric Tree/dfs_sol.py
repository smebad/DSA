# Symmetric Tree
# Depth First Search Solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (
                left.val == right.val and
                dfs(left.left, right.right) and
                dfs(left.right, right.left)
            )
        return dfs(root.left, root.right)
    
# Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
# Space Complexity: O(h), where h is the height of the tree. This space is used by the recursion stack.
# This dfs approach effectively checks for symmetry by comparing nodes in a mirrored fashion.


# Test Cases:
if __name__ == "__main__":
    sol = Solution()

    # Helper function
    def build_tree(nodes):
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while queue and i < len(nodes):
            current = queue.pop(0)
            if nodes[i] is not None:
                current.left = TreeNode(nodes[i])
                queue.append(current.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                current.right = TreeNode(nodes[i])
                queue.append(current.right)
            i += 1
        return root

    # Test Case 1
    tree1 = build_tree([1,2,2,3,4,4,3])
    assert sol.isSymmetric(tree1) == True 

    # Test Case 2
    tree2 = build_tree([1,2,2,None,3,None,3])
    assert sol.isSymmetric(tree2) == False
    print("All test cases passed.")
