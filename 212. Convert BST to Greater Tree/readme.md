# Convert BST to Greater Tree LeetCode

## 1. Problem Overview

The **Convert BST to Greater Tree** problem asks us to modify a Binary Search Tree (BST) so that every node’s value becomes the sum of its original value plus the values of all nodes that are greater than it.

### Key BST Properties

* All values in the left subtree are smaller than the node.
* All values in the right subtree are larger than the node.
* An in-order traversal of a BST gives values in ascending order.

The challenge is to update the tree **in-place** while efficiently using these properties.

---

## 2. Code Explanation

Below is your provided solution with clear comments added to help you remember the logic later.

```python
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # This variable will store the running sum of all previously visited nodes
        # during the reverse in-order traversal
        curSum = 0

        def dfs(node):
            nonlocal curSum
            
            # Base case: if the node is None, stop recursion
            if not node:
                return

            # Step 1: Visit the right subtree first (larger values)
            dfs(node.right)

            # Step 2: Update the current node's value
            # Save the original value before updating
            tmp = node.val
            node.val += curSum

            # Step 3: Update the running sum
            curSum += tmp

            # Step 4: Visit the left subtree (smaller values)
            dfs(node.left)

        # Start DFS traversal from the root
        dfs(root)
        return root
```

---

## 3. Solution Approach and Logic

### Core Idea

To convert a BST into a Greater Tree, we need to process nodes **from the largest value to the smallest value**.

### Why Reverse In-Order Traversal?

A normal in-order traversal visits nodes in ascending order:

```
Left → Node → Right
```

To process larger values first, we reverse this order:

```
Right → Node → Left
```

This ensures:

* We visit the largest node first
* We keep a running sum of all previously visited (larger) values
* Each node is updated correctly using that sum

### Step-by-Step Logic

1. Traverse the right subtree first to reach the largest values.
2. Maintain a running sum (`curSum`) of all visited nodes.
3. Update each node’s value by adding `curSum`.
4. Add the node’s original value to `curSum`.
5. Continue traversal to the left subtree.

This guarantees every node receives the sum of all greater nodes.

### Why This Approach Works Well

* It uses the BST property directly.
* Each node is visited exactly once.
* No extra data structures are needed.

---

## 4. Time and Space Complexity

### Time Complexity

* **O(n)** where `n` is the number of nodes in the tree.
* Each node is visited exactly once during DFS traversal.

### Space Complexity

* **O(h)** where `h` is the height of the tree.
* This space is used by the recursion stack.

  * Worst case (skewed tree): `O(n)`
  * Best case (balanced tree): `O(log n)`

### Most Optimal Solution

This DFS reverse in-order traversal is the **most optimal solution** because:

* It achieves linear time complexity.
* It modifies the tree in-place.
* It avoids extra memory like arrays or hash maps.
* It fully leverages the properties of a BST.

---

## Test Case
``` python
if __name__ == "__main__":
    # Helper function to print in-order traversal of the tree
    def print_inorder(node):
        if not node:
            return
        print_inorder(node.left)
        print(node.val, end=' ')
        print_inorder(node.right)

    # Test Case 1
    root1 = TreeNode(4)
    root1.left = TreeNode(1)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(2)
    root1.left.right.right = TreeNode(3)
    root1.right.left = TreeNode(5)
    root1.right.right = TreeNode(7)
    root1.right.right.right = TreeNode(8)

    solution = Solution()
    new_root1 = solution.convertBST(root1)
    print("In-order traversal of Greater Tree for Test Case 1:")
    print_inorder(new_root1)  # Expected output: 36 36 35 33 30 26 21 15 8
    print()

    # Test Case 2
    root2 = TreeNode(0)
    root2.right = TreeNode(1)

    new_root2 = solution.convertBST(root2)
    print("In-order traversal of Greater Tree for Test Case 2:")
    print_inorder(new_root2)  # Expected output: 1 1
    print()
```