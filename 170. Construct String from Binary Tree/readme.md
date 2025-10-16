# Construct String from Binary Tree - LeetCode

## Problem Explanation

The **Construct String from Binary Tree** problem requires converting a binary tree into a string that follows specific rules. The conversion is done using a **preorder traversal** (root → left → right), and the structure must be represented accurately using parentheses.

### The Rules

1. **Each node** is represented by its integer value.
2. **Children** are enclosed in parentheses:

   * If a node has a **left child**, it appears inside parentheses right after the node’s value.
   * If a node has a **right child**, it also appears in parentheses after the left child.
3. **Empty Parentheses Handling**:

   * If a node has **no children**, no parentheses are added.
   * If a node has a **right child but no left child**, an **empty pair of parentheses `()`** must be added before the right child to preserve the structure.
   * Empty parentheses are **omitted** when unnecessary (like when only a left child exists).

### Example 1

**Input:** `root = [1,2,3,4]`
**Output:** `"1(2(4))(3)"`
Explanation: Without removing empty parentheses, it would look like `1(2(4)())(3()())`. After omitting empty pairs, we get `1(2(4))(3)`.

### Example 2

**Input:** `root = [1,2,3,null,4]`
**Output:** `"1(2()(4))(3)"`
Explanation: The empty parentheses after `2` are necessary to indicate that `2` has no left child but does have a right child.

---

## Code with Comments

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []  # This list will store the characters of the resulting string

        def preorder(root):
            if not root:
                return
            
            # Add an opening parenthesis before the node value
            res.append("(")
            res.append(str(root.val))  # Add current node value
            
            # If there is a right child but no left child, we must include empty parentheses
            if not root.left and root.right:
                res.append("()")
            
            # Recurse for left and right children
            preorder(root.left)
            preorder(root.right)
            
            # Add a closing parenthesis after visiting both children
            res.append(")")

        preorder(root)
        
        # The first and last parentheses are unnecessary, so we remove them
        return "".join(res)[1:-1]
```

---

## Approach and Logic

This solution uses **Depth-First Search (DFS)** in a **preorder traversal** (visit node → left → right). The logic is straightforward:

1. Start at the root node.
2. Add the node’s value to the result string.
3. Recursively call the function for the left and right subtrees.
4. Add parentheses around the left and right subtree values to represent the structure.
5. Handle the case where a node has a right child but no left child — insert `()` to keep the mapping correct.
6. Build the final string by joining the collected parts.

This ensures that the resulting string can be mapped back to the original binary tree without ambiguity.

---

## Time and Space Complexity

| Operation            | Complexity | Explanation                                                                  |
| -------------------- | ---------- | ---------------------------------------------------------------------------- |
| **Time Complexity**  | O(n)       | Each node is visited once in the DFS traversal.                              |
| **Space Complexity** | O(n)       | Space is used by the recursion stack (up to height of tree) and result list. |

### Optimality

The provided **DFS approach** is optimal because:

* It visits each node only once.
* It constructs the result efficiently using a list instead of multiple string concatenations.
* It preserves the exact tree structure as required by the problem.

---

### Test Cases
```python
# Test Cases
solution = Solution()

# Test Case 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
print(solution.tree2str(root1))  # Output: "1(2(4))(3)"

# Test Case 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.right.right = TreeNode(4)
print(solution.tree2str(root2))  # Output: "1(2())(3(4()))"
```