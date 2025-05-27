# Construct Binary Tree from Preorder and Inorder Traversal
# Depth First Search Solution:

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root
    

# Time Complexity: O(n^2) because for each node, we are using the index method to find the index of the root in the inorder list, which takes O(n) time. Since we do this for each of the n nodes, the overall time complexity becomes O(n^2).
# Space Complexity: O(n) for the recursion stack and the space used by the output tree.
# This solution is not optimal for large trees due to the O(n^2) time complexity, but it is straightforward and easy to understand. For larger trees, a more efficient approach using a hashmap to store indices of inorder elements can be implemented to achieve O(n) time complexity.


# Test Case:
# Utility function to print the tree in level-order for verification
from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

# Test Case 1: Example 1
preorder1 = [3, 9, 20, 15, 7]
inorder1 = [9, 3, 15, 20, 7]

# Test Case 2: Example 2
preorder2 = [-1]
inorder2 = [-1]

# Instantiate solution
solution = Solution()

# Run Example 1
tree1 = solution.buildTree(preorder1, inorder1)
print("Example 1 Output:", level_order_traversal(tree1))  # Expected: [3, 9, 20, None, None, 15, 7]

# Run Example 2
tree2 = solution.buildTree(preorder2, inorder2)
print("Example 2 Output:", level_order_traversal(tree2))  # Expected: [-1]


