# Leaf-Similar Trees - LeetCode

## 1. Problem Explanation

The **Leaf-Similar Trees** problem compares two binary trees based on the sequence of their leaf nodes. A **leaf** is a node with no left or right child. When we list all leaf nodes from **left to right**, we get the tree's **leaf value sequence**.

Two binary trees are called **leaf-similar** if their leaf sequences are exactly the same.

The task:
Given two binary trees `root1` and `root2`, return `true` only if they have identical leaf sequences.

---

## 2. Explanation of the Code 

```python
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaf):
            # If the current node is null, do nothing
            if not root:
                return

            # If the node is a leaf (no children), record its value
            if not root.left and not root.right:
                leaf.append(root.val)
                return

            # Otherwise continue DFS on left and right children
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        leaf1, leaf2 = [], []

        # Collect all leaf values from both trees
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        # Compare the two sequences
        return leaf1 == leaf2
```

---

## 3. Approach and Logic

### What the solution does

The solution uses **Depth-First Search (DFS)** to extract the leaf nodes from each tree. After collecting all leaf values in order, it simply compares the two lists.

### Why DFS?

DFS naturally explores all branches of a tree down to the leaves, which makes it perfect for identifying leaf nodes.

### Step-by-step logic

1. Start DFS from the root.
2. When visiting a node:

   * If it's a leaf, add its value to a list.
   * If it's not a leaf, recursively explore left and right children.
3. Repeat this for both trees.
4. Compare the two leaf lists:

   * If identical, return `True`.
   * Otherwise, return `False`.

---

## 4. Time and Space Complexity

### Time Complexity: **O(m + n)**

* `m` = number of nodes in the first tree
* `n` = number of nodes in the second tree
* We must traverse each tree once to find all leaves.

### Space Complexity: **O(h1 + h2)**

* `h1` = height of tree1
* `h2` = height of tree2
* This comes from the recursion stack used during DFS.

In the worst case (skewed tree), height = number of nodes.
In the best case (balanced tree), height = log(number of nodes).

### Why this solution is optimal

* Any valid solution must **at least inspect every leaf**, and leaves may be anywhere, so traversal is unavoidable.
* DFS is efficient because it goes directly to leaves without storing unnecessary nodes.
* No extra data structures (like queues or maps) are used, keeping space minimal.

Thus, the DFS approach is both **simple** and **optimal** for this problem.

---

## 5. Test Cases

```python
if __name__ == "__main__":
    # Test Case 1:
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)

    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(2)
    root2.right.right.left = TreeNode(9)
    root2.right.right.right = TreeNode(8)

    sol = Solution()
    print(sol.leafSimilar(root1, root2))  # Output: True

    # Test Case 2:
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)

    root4 = TreeNode(1)
    root4.left = TreeNode(3)
    root4.right = TreeNode(2)

    print(sol.leafSimilar(root3, root4))  # Output: False
```