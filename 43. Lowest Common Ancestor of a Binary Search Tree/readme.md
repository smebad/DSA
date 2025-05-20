# Lowest Common Ancestor of a Binary Search Tree (BST) - LeetCode

## Problem Description

Given a **Binary Search Tree (BST)**, find the **lowest common ancestor (LCA)** of two given nodes `p` and `q` in the BST.

According to the definition of LCA from Wikipedia:

> "The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."

### Examples:

**Example 1:**

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
```

Explanation: The LCA of nodes 2 and 8 is 6.

**Example 2:**

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
```

Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself.

**Example 3:**

```
Input: root = [2,1], p = 2, q = 1
Output: 2
```

### Constraints:

* Number of nodes: \[2, 10^5]
* Node values are unique
* -10^9 <= Node.val <= 10^9
* Both `p` and `q` are guaranteed to exist in the BST

---

## Iterative Solution

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            # If both nodes are greater than current node, LCA is in right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # If both nodes are smaller than current node, LCA is in left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                # One node on each side or match found; current node is LCA
                return cur
```

### Explanation:

* Start from the root.
* Move to the right if both values are greater than root.
* Move to the left if both values are smaller than root.
* If they split or match the current node, that node is the LCA.

---

## Recursive Solution

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        # Both nodes less than root -> search left subtree
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # Both nodes greater than root -> search right subtree
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # One node on each side or equal to current root
            return root
```

---

## Approach & Logic

Both solutions utilize the properties of a Binary Search Tree:

* All nodes in the left subtree of a node are smaller.
* All nodes in the right subtree are larger.

By comparing the values of `p` and `q` with the current node, we can efficiently find the split point which is the **Lowest Common Ancestor**.

### Differences:

* **Iterative:** Uses a loop; preferred for space efficiency.
* **Recursive:** More elegant and readable; uses call stack for recursion.

---

## Time and Space Complexity

### Time Complexity:

* **Both Iterative and Recursive:** O(h), where `h` is the height of the BST.

  * In a balanced BST, `h = log(n)`
  * In the worst case (skewed tree), `h = n`

### Space Complexity:

* **Iterative:** O(1)
* **Recursive:** O(h) due to call stack

### Most Optimal:

* **Iterative** is more optimal in terms of space since it avoids stack overhead, making it suitable for large trees.

---

## Test Cases

```python
# Test Case 1:
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root.left
q = root.right
print(Solution().lowestCommonAncestor(root, p, q))  # Output: 6

# Test Case 2:
p = root.left
q = root.left.right
print(Solution().lowestCommonAncestor(root, p, q))  # Output: 2

# Test Case 3:
root = TreeNode(2)
root.left = TreeNode(1)
p = root.left
q = root
print(Solution().lowestCommonAncestor(root, p, q))  # Output: 2
```

---

## Summary

The Lowest Common Ancestor problem in BSTs is efficiently solved by leveraging the ordered structure of BSTs. Both iterative and recursive solutions perform in O(h) time, with iterative being more space-efficient. Understanding this pattern is critical for mastering DSA problems involving binary trees.
