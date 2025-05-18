# Same Tree - LeetCode

## Problem Statement

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if:

* They are structurally identical.
* The nodes have the same value.

### Example 1:

**Input:** p = \[1,2,3], q = \[1,2,3]
**Output:** True

### Example 2:

**Input:** p = \[1,2], q = \[1,null,2]
**Output:** False

### Example 3:

**Input:** p = \[1,2,1], q = \[1,1,2]
**Output:** False

### Constraints:

* The number of nodes in both trees is in the range \[0, 100].
* `-10^4 <= Node.val <= 10^4`

---

## Solution 1: Depth First Search (DFS)

### Code Explanation with Comments:

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, trees are identical up to this point
        if not p and not q:
            return True

        # If both nodes are not None and have the same value
        if p and q and p.val == q.val:
            # Recursively check left and right subtrees
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            # Trees are not the same
            return False
```

### Approach:

* This solution uses a recursive depth-first traversal.
* At each step, it compares the current node of `p` and `q`.
* If they match, it recursively checks the left and right children.

### Time Complexity:

* **O(n)**: where `n` is the number of nodes. Each node is visited once.

### Space Complexity:

* **O(h)**: where `h` is the height of the tree.

  * In worst-case (skewed tree): O(n)
  * In best-case (balanced tree): O(log n)

---

## Solution 2: Breadth First Search (BFS)

### Code Explanation with Comments:

```python
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])  # Queue for tree p
        q2 = deque([q])  # Queue for tree q

        while q1 and q2:
            nodeP = q1.popleft()
            nodeQ = q2.popleft()

            # If both are None, continue to next nodes
            if nodeP is None and nodeQ is None:
                continue
            # If one is None or values are different, trees are not same
            if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                return False

            # Add children to respective queues
            q1.append(nodeP.left)
            q1.append(nodeP.right)
            q2.append(nodeQ.left)
            q2.append(nodeQ.right)

        return True  # All nodes matched
```

### Approach:

* This solution uses a queue for level-by-level comparison.
* At each step, it dequeues nodes from both trees and compares them.

### Time Complexity:

* **O(n)**: Each node is visited once.

### Space Complexity:

* **O(n)**: Queue stores up to `n` nodes in the worst case.

---

## Comparison of DFS vs BFS

| Feature            | DFS (Recursive)        | BFS (Iterative) |
| ------------------ | ---------------------- | --------------- |
| Time Complexity    | O(n)                   | O(n)            |
| Space Complexity   | O(h)                   | O(n)            |
| Simplicity         | Simple, elegant        | More verbose    |
| Use of Stack/Queue | Recursion (call stack) | Explicit queue  |

### Most Optimal Solution:

* **DFS (recursive)** is typically more space-efficient for balanced trees due to lower space usage (O(log n)).
* It is also simpler to write and understand.
* **However**, BFS may be preferred if stack overflow is a concern with deep recursion.

---

## Test Cases:

```python
# Test Case 1:
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
print(Solution().isSameTree(root1, root2)) # True

# Test Case 2:
root3 = TreeNode(1)
root3.left = TreeNode(2)

root4 = TreeNode(1)
root4.right = TreeNode(2)
print(Solution().isSameTree(root3, root4)) # False

# Test Case 3:
root5 = TreeNode(1)
root5.left = TreeNode(2)
root5.right = TreeNode(1)

root6 = TreeNode(1)
root6.left = TreeNode(1)
root6.right = TreeNode(2)
print(Solution().isSameTree(root5, root6)) # False
```

---

## Conclusion

Both DFS and BFS solutions are valid and efficient for the "Same Tree" problem. The choice between them depends on the scenario:

* **Use DFS** when you prefer simpler code and lower space complexity for balanced trees.
* **Use BFS** when you want to avoid deep recursion or process trees level by level.

This problem helps in building a deeper understanding of tree traversal techniques and how to compare structures and values in binary trees.
