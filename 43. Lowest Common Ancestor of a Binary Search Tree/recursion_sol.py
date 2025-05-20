# Lowest Common Ancestor of a Binary Search Tree
# Recursive solution:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
            

# Time complexity: O(h), where h is the height of the tree. This is because we are traversing the tree from the root to the lowest common ancestor, which takes O(h) time in the worst case.
# Space complexity: O(h), where h is the height of the tree. This is because we are using recursion, which adds to the call stack. In the worst case, the height of the tree can be equal to the number of nodes in the tree, leading to O(n) space complexity.
# This recursive solution is efficient and works well for large binary search trees.
# The recursive approach is more elegant and easier to understand, but it may not be as efficient in terms of space complexity compared to the iterative approach.


# Test Cases:
# Test Case 1:
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root.left
q = root.right

sol = Solution()
print(sol.lowestCommonAncestor(root, p, q))  # Output: 6

# Test Case 2:
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root.left
q = root.left.right

sol = Solution()
print(sol.lowestCommonAncestor(root, p, q))  # Output: 2

# Test Case 3:
root = TreeNode(2)
root.left = TreeNode(1)

p = root.left
q = root

sol = Solution()
print(sol.lowestCommonAncestor(root, p, q))  # Output: 2
