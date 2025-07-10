# Insert into a Binary Search Tree - LeetCode

## Problem Description

"Insert into a Binary Search Tree" is a classic data structure problem where you are given the root of a Binary Search Tree (BST) and a value to insert. The task is to insert the given value into the BST while maintaining its properties and return the updated root node.

A Binary Search Tree is a binary tree where each node's value is greater than all values in its left subtree and less than all values in its right subtree.

### Constraints:

* The number of nodes in the tree is in the range \[0, 10^4].
* Node values are unique.
* -10^8 <= Node.val, val <= 10^8
* It's guaranteed that `val` does not exist in the original BST.

## Code Explanation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)  # If tree is empty, create a new node

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)  # Recur right
        else:
            root.left = self.insertIntoBST(root.left, val)  # Recur left

        return root
```

## Approach and Logic

There are two main solutions to this problem: Recursive and Iterative.

### Recursive Approach

1. If the root is `None`, insert the value here as a new node.
2. If the value is greater than the current node's value, recurse right.
3. If the value is less than the current node's value, recurse left.
4. Finally, return the root node.

This approach uses the call stack to keep track of traversal, making it simple and readable.

### Iterative Approach

```python
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        cur = root
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left
```

This version avoids recursion and uses a while loop to locate the appropriate position to insert the new node.

## Time and Space Complexity

### Recursive Solution

* **Time Complexity:** O(h), where h is the height of the tree. In the worst case (completely unbalanced tree), h = n.
* **Space Complexity:** O(h), due to recursion stack.

### Iterative Solution

* **Time Complexity:** O(h), same as the recursive one.
* **Space Complexity:** O(1), as no extra space (besides a few pointers) is used.

## Optimality

The iterative solution is more space-efficient because it does not use the call stack for recursion. It is considered optimal for large input sizes and systems with stack size limitations.

## Test Cases

```python
# Test Case 1:
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
val = 5
sol = Solution()
new_root = sol.insertIntoBST(root, val)  # Should insert 5 as right child of 4's left child (3 not present)

# Test Case 2:
root = TreeNode(40)
root.left = TreeNode(20)
root.right = TreeNode(60)
val = 25
sol = Solution()
new_root = sol.insertIntoBST(root, val)  # Should insert 25 as right child of 20
```
