# Construct Binary Tree from Preorder and Inorder Traversal - LeetCode

## Problem Description

Given two integer arrays `preorder` and `inorder`, where:

* `preorder` is the preorder traversal of a binary tree
* `inorder` is the inorder traversal of the same tree

Your task is to construct and return the binary tree.

### Preorder Traversal

Visit the root first, then the left subtree, then the right subtree.

### Inorder Traversal

Visit the left subtree first, then the root, then the right subtree.

### Example 1:

**Input:**

```
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
```

**Output:**

```
[3, 9, 20, null, null, 15, 7]
```

### Example 2:

**Input:**

```
preorder = [-1]
inorder = [-1]
```

**Output:**

```
[-1]
```

### Constraints:

* 1 <= preorder.length <= 3000
* preorder.length == inorder.length
* -3000 <= preorder\[i], inorder\[i] <= 3000
* All values are unique
* preorder and inorder represent a valid binary tree

---

## Code Explanation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None  # Base case: if either list is empty, return None

        root = TreeNode(preorder[0])  # First value in preorder is the root
        mid = inorder.index(preorder[0])  # Find root index in inorder list

        # Recursively build left and right subtrees
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root
```

---

## Approach and Logic

### Approach:

1. The first value of the preorder list is always the root of the current subtree.
2. Find the index of this root value in the inorder list. This divides the inorder list into:

   * Left subtree (elements before the root index)
   * Right subtree (elements after the root index)
3. Use recursion to construct left and right subtrees with respective slices of preorder and inorder lists.

### Why It Works:

The preorder list gives the root at each level, and the inorder list tells us how to split the tree into left and right parts. By combining both, we can rebuild the tree accurately.

---

## Time and Space Complexity

### Provided Solution:

* **Time Complexity:** O(n^2)

  * The `inorder.index()` operation is O(n) and is called for every node.
  * For `n` nodes, this results in O(n^2).

* **Space Complexity:** O(n)

  * Due to the recursive call stack and space required for storing the tree.

---

## Summary

* The problem requires rebuilding a binary tree from preorder and inorder traversal arrays.
* The basic solution is simple but has O(n^2) time complexity.
* Understanding the traversal order logic is crucial to solving this problem.
