# Convert Sorted Array to Binary Search Tree - LeetCode

## Problem Explanation

The problem **Convert Sorted Array to Binary Search Tree** requires us to take a sorted array (in ascending order) and construct a **height-balanced Binary Search Tree (BST)** from it.

A **height-balanced BST** is defined as a binary tree where the depth of the two subtrees of every node never differs by more than 1. This ensures that the tree remains balanced, leading to efficient operations such as search, insertion, and deletion.

### Problem Statement

* Input: A sorted integer array `nums`.
* Output: A height-balanced BST constructed from the array.

**Example 1:**

```
Input: nums = [-10, -3, 0, 5, 9]
Output: [0, -3, 9, -10, null, 5]
```

**Example 2:**

```
Input: nums = [1, 3]
Output: [3, 1]
```

### Constraints

* 1 <= nums.length <= 10^4
* -10^4 <= nums[i] <= 10^4
* `nums` is sorted in strictly increasing order.

---

## Code with Comments

```python
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # Helper function to build BST recursively
        def helper(l, r):
            if l > r:
                return None  # Base case: no elements left

            # Choose middle element to maintain balance
            m = (l + r) // 2
            root = TreeNode(nums[m])

            # Recursively build left and right subtrees
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root

        return helper(0, len(nums) - 1)
```

---

## Solution Approach

### Logic

1. Since the input array is sorted, the **middle element** is always the best candidate for the root of the BST. This ensures that elements on the left side are smaller and elements on the right side are larger, maintaining the BST property.
2. We recursively:

   * Pick the middle element of the array as the root.
   * Build the left subtree from the left half of the array.
   * Build the right subtree from the right half of the array.
3. This recursion continues until all elements are placed in the tree.

### Example Walkthrough

For `nums = [-10, -3, 0, 5, 9]`:

* Middle element is `0` → root.
* Left half is `[-10, -3]` → recursive call → middle `-3` → left child.
* Right half is `[5, 9]` → recursive call → middle `9` → right child.
* Subtrees are built recursively.

Final Tree:

```
        0
       / \
    -3    9
    /    /
 -10    5
```

### Why This Works

This approach always chooses the middle element, which ensures that the tree remains balanced, satisfying the requirement of a height-balanced BST.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`

  * Each element is processed exactly once to create a tree node.
  * Therefore, for `n` elements, the total time is `O(n)`.

* **Space Complexity:** `O(log n)` (for recursion stack in a balanced tree)

  * At most, the depth of recursion is `O(log n)` for a balanced tree.
  * In the worst case (unbalanced tree), it could be `O(n)`. But since we always pick the middle, the tree stays balanced.

---

## Optimality

* This recursive **divide-and-conquer approach** is optimal because:

  * It guarantees the BST is balanced.
  * It minimizes the height difference between subtrees.
  * Time complexity cannot be improved beyond `O(n)` because we must process all elements.

Thus, this solution is the most efficient for the problem.

---

## Test Cases

```python
solution = Solution()

# Test Case 1:
nums1 = [-10, -3, 0, 5, 9]
result1 = solution.sortedArrayToBST(nums1)
print(result1.val)          # Expected Output: 0
print(result1.left.val)     # Expected Output: -3
print(result1.right.val)    # Expected Output: 9
print(result1.left.left.val) # Expected Output: -10
print(result1.right.left)    # Expected Output: None
print(result1.right.right.val) # Expected Output: 5

# Test Case 2:
nums2 = [1, 3]
result2 = solution.sortedArrayToBST(nums2)
print(result2.val)          # Expected Output: 3
print(result2.left)         # Expected Output: None
print(result2.right.val)    # Expected Output: 1
```