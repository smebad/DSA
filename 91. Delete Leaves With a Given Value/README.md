# Delete Leaves With a Given Value - LeetCode

## Problem Statement

Given the root of a binary tree and an integer `target`, delete **all the leaf nodes** with the value equal to `target`. A node is considered a leaf if it has no children. Importantly, after deleting such a leaf node, if its parent becomes a leaf and has the same value as `target`, that parent node should also be deleted. This process must be repeated until no more deletions are possible.

### Example 1:

```
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
```

### Example 2:

```
Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
```

### Example 3:

```
Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
```

## Constraints

* The number of nodes in the tree is in the range \[1, 3000].
* 1 <= Node.val, target <= 1000

---

## Recursive (Post-Order) Solution

### Python Code with Comments

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None  # If the node is None, nothing to process

        # Recursively process the left and right subtree
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # If the node becomes a leaf and has the target value, delete it
        if not root.left and not root.right and root.val == target:
            return None

        return root  # Return the potentially modified tree
```

### Approach and Explanation

* We use **post-order traversal** (left -> right -> root).
* We recursively clean up the children before checking the current node.
* If a node becomes a leaf and has the value equal to `target`, it is deleted (returned as `None`).
* This continues recursively, allowing parent nodes to be removed if they become target leaves after their children are removed.

### Time and Space Complexity

* **Time Complexity:** O(n), where n is the number of nodes. Every node is visited once.
* **Space Complexity:** O(h), where h is the height of the tree (due to recursion stack). In the worst case (skewed tree), h = n.

---

## Iterative (Post-Order) Solution

### Python Code with Comments

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [root]  # Stack for traversal
        visit = set()  # To track visited nodes
        parents = {root: None}  # To map each node to its parent

        while stack:
            node = stack.pop()
            # Process leaf node
            if not node.left and not node.right:
                if node.val == target:
                    p = parents[node]
                    if not p:
                        return None  # Root is being deleted
                    if p.left == node:
                        p.left = None
                    if p.right == node:
                        p.right = None
            elif node not in visit:
                # Mark node as visited and revisit after its children
                visit.add(node)
                stack.append(node)  # Push current node again for post-processing
                if node.left:
                    stack.append(node.left)
                    parents[node.left] = node
                if node.right:
                    stack.append(node.right)
                    parents[node.right] = node

        return root
```

### Approach and Explanation

* Simulates **post-order traversal** using a stack.
* Tracks parent relationships to remove child links during traversal.
* Uses a `visit` set to control post-order logic (process node after children).
* If a leaf node matches the target, remove its link from the parent.

### Time and Space Complexity

* **Time Complexity:** O(n), where n is the number of nodes.
* **Space Complexity:** O(n), for the stack, parent mapping, and visited set.

---

## Comparison of Solutions

| Aspect      | Recursive Solution        | Iterative Solution                            |
| ----------- | ------------------------- | --------------------------------------------- |
| Traversal   | Post-order                | Simulated Post-order                          |
| Simplicity  | More readable and concise | Slightly complex due to manual stack handling |
| Stack Space | O(h) (recursion stack)    | O(n) (explicit stack and hash maps)           |
| Performance | Optimal                   | Optimal                                       |

### Which is More Optimal?

* **Both solutions have the same time complexity: O(n)**.
* **Recursive solution uses less auxiliary memory** (O(h) vs O(n)) in a balanced tree.
* **Recursive approach is simpler and typically preferred**, unless recursion depth is a concern (e.g., very deep trees where stack overflow can occur).

---

## Summary

* This problem uses post-order traversal to remove leaf nodes with a specific value.
* Removing nodes can cause parent nodes to become leaves, so we must repeat the process recursively or simulate it iteratively.
* The recursive solution is optimal and cleaner, making it preferable for most practical scenarios.
* Understanding tree traversal and recursive logic is key to solving this efficiently.
