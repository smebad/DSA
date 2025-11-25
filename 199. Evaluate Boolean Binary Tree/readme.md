# Evaluate Boolean Binary Tree - LeetCode

## Problem Description

**Evaluate Boolean Binary Tree** is a problem where you are given the root of a full binary tree. Each node in the tree has the following properties:

* **Leaf nodes** have a value of `0` or `1`, where `0` represents `False` and `1` represents `True`.
* **Non-leaf nodes** have a value of `2` or `3`, where `2` represents a boolean `OR` and `3` represents a boolean `AND`.

The evaluation of the tree follows these rules:

1. If the node is a leaf node, the evaluation is its value (`True` for `1` and `False` for `0`).
2. Otherwise, evaluate the left and right children, and then apply the boolean operation (`OR` or `AND`) indicated by the node's value.

The task is to return the boolean result of evaluating the root node.

### Example 1

```
Input: root = [2,1,3,null,null,0,1]
Output: true
```

Explanation:

* The AND node evaluates `False AND True = False`.
* The OR node evaluates `True OR False = True`.
* The root node evaluates to `True`.

### Example 2

```
Input: root = [0]
Output: false
```

Explanation:

* The root node is a leaf node with value 0, so it evaluates to `False`.

## Code Explanation

```python
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # If the node is a leaf node (no children), return True if its value is 1, else False
        if not root.left:
            return root.val == 1

        # If the node value is 2, perform OR operation on left and right subtrees
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)

        # If the node value is 3, perform AND operation on left and right subtrees
        if root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
```

### Comments on the Code

* `if not root.left:`: Checks if the node is a leaf. Leaf nodes have no children.
* `root.val == 1`: Converts the leaf node value into boolean (`1` to `True`, `0` to `False`).
* `root.val == 2` / `root.val == 3`: Determines which boolean operation to apply.
* `self.evaluateTree(root.left/right)`: Recursively evaluates the left and right children.

## Approach and Logic

The solution uses **Depth-First Search (DFS)** to recursively evaluate the tree:

1. **Leaf node evaluation**: Directly return `True` if value is `1` or `False` if `0`.
2. **Internal node evaluation**:

   * If value is `2`, recursively evaluate the left and right children and return `OR`.
   * If value is `3`, recursively evaluate the left and right children and return `AND`.

This recursion ensures that each subtree is evaluated according to the rules before combining the results at the parent nodes.

### Why this approach works

* DFS naturally evaluates subtrees before their parent nodes.
* Each node is visited exactly once, and the boolean operations are applied correctly.
* The tree is full, so each non-leaf node has exactly two children, which simplifies recursion.

## Time and Space Complexity

* **Time Complexity**: `O(n)`

  * Each node is visited once to compute its value.
  * `n` is the total number of nodes in the tree.

* **Space Complexity**: `O(h)`

  * Recursion stack takes up to `h` space, where `h` is the height of the tree.
  * In the worst case (skewed tree), `h = n`, giving `O(n)` space.
  * For balanced trees, `h = log(n)`.

## Test Cases

```python
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(1)
    print(sol.evaluateTree(root1))  # Output: True

    # Test Case 2
    root2 = TreeNode(0)
    print(sol.evaluateTree(root2))  # Output: False
```