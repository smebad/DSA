# Construct String from Binary Tree
# Given the root node of a binary tree, your task is to create a string representation of the tree following a specific set of formatting rules. The representation should be based on a preorder traversal of the binary tree and must adhere to the following guidelines:

# Node Representation: Each node in the tree should be represented by its integer value.

# Parentheses for Children: If a node has at least one child (either left or right), its children should be represented inside parentheses. Specifically:

# If a node has a left child, the value of the left child should be enclosed in parentheses immediately following the node's value.
# If a node has a right child, the value of the right child should also be enclosed in parentheses. The parentheses for the right child should follow those of the left child.
# Omitting Empty Parentheses: Any empty parentheses pairs (i.e., ()) should be omitted from the final string representation of the tree, with one specific exception: when a node has a right child but no left child. In such cases, you must include an empty pair of parentheses to indicate the absence of the left child. This ensures that the one-to-one mapping between the string representation and the original binary tree structure is maintained.

# In summary, empty parentheses pairs should be omitted when a node has only a left child or no children. However, when a node has a right child but no left child, an empty pair of parentheses must precede the representation of the right child to reflect the tree's structure accurately.

 

# Example 1:


# Input: root = [1,2,3,4]
# Output: "1(2(4))(3)"
# Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the empty parenthesis pairs. And it will be "1(2(4))(3)".
# Example 2:


# Input: root = [1,2,3,null,4]
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, except the () after 2 is necessary to indicate the absence of a left child for 2 and the presence of a right child.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -1000 <= Node.val <= 1000


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