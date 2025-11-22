# Merge Two Binary Trees - LeetCode

## 1. Problem Explanation

The "Merge Two Binary Trees" problem gives you two binary trees and asks you to merge them into a single new tree.

The merging process follows a simple rule:

* If both trees have a node at the same position, you add their values together and create a new node with that sum.
* If only one of the trees has a node at a position, you use that existing node directly.

The merging must start from the two root nodes and continue recursively down both trees.

This ensures every position in the new tree correctly represents a combination of the two input trees.

---

## 2. Code Explanation with Comments

Below is your code with added comments to help you remember how the solution works:

```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # If both nodes are null, there is nothing to merge.
        if not root1 and not root2:
            return None

        # Get the value from each tree's node, or 0 if the node does not exist.
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0

        # Create a new node with the sum of the values.
        root = TreeNode(v1 + v2)

        # Recursively merge the left children of both trees.
        root.left = self.mergeTrees(
            root1.left if root1 else None,
            root2.left if root2 else None,
        )

        # Recursively merge the right children of both trees.
        root.right = self.mergeTrees(
            root1.right if root1 else None,
            root2.right if root2 else None,
        )

        # Return the newly created merged node.
        return root
```

---

## 3. Solution Approach and Logic

This solution uses **Depth First Search (DFS)** and recursion. The core idea is to merge trees from the top down.

### Step-by-step logic:

1. **Start from both roots.**
   If both nodes are `null`, there is nothing to add, so return `None`.

2. **Add node values.**

   * If both nodes exist, add their values.
   * If only one exists, use its value (the other contributes 0).

3. **Create a new node.**
   A fresh node is created to store the merged value.

4. **Merge left subtrees recursively.**
   Call `mergeTrees` on:

   * `root1.left` and `root2.left`.

5. **Merge right subtrees recursively.**
   Call `mergeTrees` on:

   * `root1.right` and `root2.right`.

6. **Return the merged node.**

### Why this works

Recursion naturally mirrors the structure of the binary tree, making it straightforward to walk both trees at once.

### Differences from other approaches

There are two main ways to solve this problem:

#### 1. DFS (Recursive) – Used in your code

* Easy to write and understand.
* Follows tree structure naturally.
* Uses recursion to explore each node.

#### 2. BFS (Iterative)

* Uses a queue to traverse both trees level by level.
* Can be harder to write and maintain.
* Avoids recursion for environments with restricted call stack size.

Your solution is the simpler and more intuitive recursive DFS version.

---

## 4. Time and Space Complexity

### Time Complexity: **O(m + n)**

Where:

* `m` = number of nodes in tree 1
* `n` = number of nodes in tree 2

You may end up visiting all nodes in both trees. Each node is processed once, which is optimal because you cannot merge trees without examining all nodes.

### Space Complexity: **O(h)** (h = height of the taller tree)

This space comes from the **recursion call stack**.

Worst case:

* The tree is skewed (like a linked list): height = number of nodes → O(m + n)

Best case:

* Trees are balanced → O(log(m + n))

### Why this is optimal

You must at least touch every node of both trees to produce the merged result, so the time complexity cannot be improved below O(m + n).

The space complexity is also minimal for a DFS recursion because no extra data structures are created; only the recursion stack is used.

## 5. Test Cases:
```python
def build_tree_from_list(lst):
    if not lst:
        return None
    nodes = [TreeNode(x) if x is not None else None for x in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

sol = Solution()

# Test Case 1:
root1 = build_tree_from_list([1,3,2,5])
root2 = build_tree_from_list([2,1,3,None,4,None,7])
merged_tree = sol.mergeTrees(root1, root2)
print(tree_to_list(merged_tree))  # Output: [3, 4, 5, 5, 4, None, 7]

# Test Case 2:
root1 = build_tree_from_list([1])
root2 = build_tree_from_list([1,2])
merged_tree = sol.mergeTrees(root1, root2)
print(tree_to_list(merged_tree))  # Output: [2, 2]
```