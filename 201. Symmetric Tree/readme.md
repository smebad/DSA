# Symmetric Tree - LeetCode

## Problem Description

The **Symmetric Tree** problem asks us to determine if a given binary tree is a mirror of itself. In other words, a tree is symmetric if the left subtree is a mirror reflection of the right subtree.

A tree is considered symmetric if:

* Its left and right subtrees are structurally identical.
* Corresponding nodes in the left and right subtrees have the same value.

### Examples

**Example 1:**

```
Input: root = [1,2,2,3,4,4,3]
Output: true
```

**Explanation:**
The tree is symmetric about its center.

**Example 2:**

```
Input: root = [1,2,2,null,3,null,3]
Output: false
```

**Explanation:**
The left and right subtrees are not mirrors of each other.

### Constraints

* The number of nodes in the tree is in the range [1, 1000].
* Node values are in the range [-100, 100].

## Code Explanation

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            # If both nodes are None, they are symmetric
            if not left and not right:
                return True
            # If one is None and the other is not, not symmetric
            if not left or not right:
                return False
            # Nodes are symmetric if values match and subtrees are mirrors
            return (
                left.val == right.val and
                dfs(left.left, right.right) and
                dfs(left.right, right.left)
            )
        return dfs(root.left, root.right)
```

### Detailed Explanation

1. **Approach:**

   * Use a **Depth-First Search (DFS)** to recursively check symmetry.
   * Compare the left subtree with the right subtree in a mirrored manner:

     * `left.left` with `right.right`
     * `left.right` with `right.left`

2. **Logic:**

   * If both nodes being compared are `None`, they are symmetric.
   * If one node is `None` but the other is not, the tree is not symmetric.
   * If node values are equal, recursively check their mirrored children.

3. **Why DFS Works:**

   * DFS allows us to traverse both subtrees simultaneously.
   * At each step, it ensures that the structure and node values are mirrored.

### Complexity Analysis

* **Time Complexity:** `O(n)` where `n` is the number of nodes. Each node is visited once.
* **Space Complexity:** `O(h)` where `h` is the height of the tree, due to the recursion stack. In the worst case (skewed tree), `h = n`.

### Test Cases

```python
if __name__ == "__main__":
    sol = Solution()

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

    tree1 = build_tree([1,2,2,3,4,4,3])
    assert sol.isSymmetric(tree1) == True

    tree2 = build_tree([1,2,2,None,3,None,3])
    assert sol.isSymmetric(tree2) == False

    print("All test cases passed.")
```