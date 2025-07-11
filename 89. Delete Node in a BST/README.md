# Delete Node in a Binary Search Tree (BST) - LeetCode

## Problem Description

Given the root node of a Binary Search Tree (BST) and an integer key, the goal is to delete the node with the given key from the BST and return the updated root node.

A BST maintains the following properties:

* The left subtree of a node contains only nodes with values less than the node's value.
* The right subtree of a node contains only nodes with values greater than the node's value.
* Both the left and right subtrees must also be binary search trees.

## Problem Statement

The deletion process involves two stages:

1. **Search for the node** to remove.
2. **Delete the node** and restructure the tree if necessary to maintain BST properties.

## Examples

### Example 1:

**Input:** root = \[5,3,6,2,4,null,7], key = 3
**Output:** \[5,4,6,2,null,null,7]
**Explanation:** Node with value 3 is deleted. 4 replaces 3.

### Example 2:

**Input:** root = \[5,3,6,2,4,null,7], key = 0
**Output:** \[5,3,6,2,4,null,7]
**Explanation:** Node 0 not found, so tree remains unchanged.

### Example 3:

**Input:** root = \[], key = 0
**Output:** \[]

---

## Code Explanation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root  # If tree is empty or key not found, return None

        # Search for the node with the given key
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # Node found
            if not root.left:
                return root.right  # Replace with right child if left is None
            elif not root.right:
                return root.left  # Replace with left child if right is None

            # Node has two children: find inorder successor (smallest in right subtree)
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val  # Replace value
            # Delete the inorder successor node
            root.right = self.deleteNode(root.right, root.val)

        return root
```

## Approach and Logic

The solution uses **recursion** to search and delete the node:

1. If the key is smaller or greater than the current node's value, recurse into the left or right subtree accordingly.
2. If the node is found:

   * If it has **no left child**, return the right child.
   * If it has **no right child**, return the left child.
   * If it has **two children**, find the **inorder successor** (the smallest value in the right subtree), copy its value to the current node, and then delete the successor node recursively.

### Key Concepts:

* The **inorder successor** is used to preserve the BST properties when the node has two children.
* The function always returns the root of the (possibly modified) subtree.

## Time and Space Complexity

* **Time Complexity:** `O(h)`, where `h` is the height of the tree. In the worst case (completely unbalanced), this could be `O(n)`, and in the best case (balanced), it's `O(log n)`.
* **Space Complexity:** `O(h)` due to the recursion stack.

## Optimality

This recursive approach is optimal in both time and space for a BST delete operation. It does not require additional data structures and respects the BST properties strictly while minimizing structural changes to the tree.

## Test Cases

```python
# Test Case 1
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
key = 3
print(Solution().deleteNode(root, key))  # Output: [5,4,6,2,null,null,7]

# Test Case 2
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
key = 0
print(Solution().deleteNode(root, key))  # Output: [5,3,6,2,4,null,7]

# Test Case 3
root = None
key = 0
print(Solution().deleteNode(root, key))  # Output: []
```
