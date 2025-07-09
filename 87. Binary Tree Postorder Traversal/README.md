# Binary Tree Postorder Traversal - LeetCode

## Problem Description

Given the root of a binary tree, return the postorder traversal of its nodes' values.

**Postorder Traversal** follows the order: **left subtree -> right subtree -> root**.

## Example Inputs and Outputs

**Example 1:**

* Input: `root = [1,null,2,3]`
* Output: `[3,2,1]`

**Example 2:**

* Input: `root = [1,2,3,4,5,null,8,null,null,6,7,9]`
* Output: `[4,6,7,5,2,9,8,3,1]`

**Example 3:**

* Input: `root = []`
* Output: `[]`

**Example 4:**

* Input: `root = [1]`
* Output: `[1]`

## Constraints

* Number of nodes is in the range \[0, 100].
* Node values range from -100 to 100.

## Recursive Depth-First Search (DFS) Solution

```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(node):
            if not node:
                return
            postorder(node.left)     # Traverse left subtree
            postorder(node.right)    # Traverse right subtree
            res.append(node.val)     # Visit root node
        
        postorder(root)
        return res
```

### Time and Space Complexity

* **Time Complexity:** O(n), where n is the number of nodes.
* **Space Complexity:** O(n) due to recursion stack in worst case.

### Explanation

This method is a simple recursive approach that follows the definition of postorder traversal.

## Iterative DFS Solution Using Stack

```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        res = []

        while stack:
            cur, v = stack.pop(), visit.pop()
            if cur:
                if v:
                    res.append(cur.val)  # Process the node after children
                else:
                    stack.append(cur)
                    visit.append(True)
                    stack.append(cur.right)
                    visit.append(False)
                    stack.append(cur.left)
                    visit.append(False)

        return res
```

### Time and Space Complexity

* **Time Complexity:** O(n), visiting each node once.
* **Space Complexity:** O(n) due to the stack.

### Explanation

This solution uses a stack to simulate recursion. Each node is pushed multiple times with a flag indicating whether it should be processed or still has children to process. It effectively emulates the postorder traversal order.

## Summary

* **Postorder Traversal** visits nodes in left -> right -> root order.
* The recursive solution is simple and intuitive but uses the call stack.
* The iterative version uses an explicit stack and a flag to manage node visits.
* Both solutions have the same time and space complexity.
* **Most optimal solution:** Recursive and iterative methods are both O(n) and optimal within given constraints. The choice depends on constraints like call stack limits or recursion preference.
