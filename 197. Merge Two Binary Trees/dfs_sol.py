# Merge Two Binary Trees
# Depth First Search (DFS) solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        root = TreeNode(v1 + v2)

        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return root
    
# Time complexity: O(m + n), where m and n are the number of nodes in the two trees. In the worst case, we may need to visit all nodes in both trees.
# Space complexity: O(m + n) in the worst case, the recursion stack can go as deep as the total number of nodes in both trees.
# This depth first search (DFS) approach effectively merges the two binary trees by recursively summing the values of overlapping nodes and creating new nodes for non-overlapping ones.


# Test Cases:
def build_tree_from_list(lst):
    if not lst:
        return None
    nodes = [TreeNode(x) if x is not None else None for x in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

sol = Solution()

# Test Case 1:
root1 = build_tree_from_list([1,3,2,5])
root2 = build_tree_from_list([2,1,3,None,4,None,7])
merged_tree = sol.mergeTrees(root1, root2)
print(tree_to_list(merged_tree))  # Output: [3, 4, 5, 5, 4, None, 7]

# Test Case 2:
root1 = build_tree_from_list([1])
root2 = build_tree_from_list([1,2])
merged_tree = sol.mergeTrees(root1, root2)
print(tree_to_list(merged_tree))  # Output: [2, 2]
