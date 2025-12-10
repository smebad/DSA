# Unique Binary Search Trees - LeetCode

## 1. Problem Explanation

The **Unique Binary Search Trees** problem asks us to find how many *structurally different* Binary Search Trees (BSTs) can be formed using values from 1 to n.

A Binary Search Tree follows these rules:

* All values in the left subtree are smaller than the root.
* All values in the right subtree are greater than the root.
* Both left and right subtrees are also BSTs.

In this problem, we only care about the *structure* of the tree, not the actual values, as long as the BST property is maintained.

### Example:

* Input: n = 3
* Output: 5

There are exactly 5 different BST structures that can be created using values 1, 2, and 3.

This problem is a classic application of **Dynamic Programming** and is based on the **Catalan Number** sequence.

---

## 2. Code With Detailed Comments

```python
class Solution:
    def numTrees(self, n: int) -> int:
        # Create a DP array where numTree[i]
        # represents the number of unique BSTs with i nodes
        numTree = [1] * (n + 1)

        # Start calculating from 2 nodes up to n nodes
        for nodes in range(2, n + 1):
            total = 0  # This will store the total BSTs for 'nodes'

            # Try each number as the root
            for root in range(1, nodes + 1):
                # Number of nodes in the left subtree
                left = root - 1

                # Number of nodes in the right subtree
                right = nodes - root

                # Total BSTs formed with 'root' as root
                total += numTree[left] * numTree[right]

            # Store total BSTs possible with 'nodes' nodes
            numTree[nodes] = total

        # Return result for n nodes
        return numTree[n]
```

---

## 3. Solution Approach and Logic Explained

### Core Idea

If we choose a number `root` as the root of the BST:

* All numbers smaller than `root` go to the left subtree.
* All numbers larger than `root` go to the right subtree.

If:

* Left subtree has `L` nodes
* Right subtree has `R` nodes

Then:

Number of unique BSTs = (BSTs with L nodes) × (BSTs with R nodes)

We compute this for **every possible root** and sum the results.

---

### Step-by-Step DP Breakdown

1. `numTree[0] = 1` → An empty tree is considered one valid BST.
2. `numTree[1] = 1` → Only one possible structure.
3. For each value from 2 to n:

   * Try every number as the root.
   * Multiply left subtree possibilities with right subtree possibilities.
   * Add them together.

This builds solutions from smaller values to larger ones.

---

### Why This Works

Every BST structure is uniquely formed by:

* Choosing a root
* Combining all valid left subtree structures with all valid right subtree structures

This guarantees that all unique BST structures are counted exactly once.

---

## 4. Time and Space Complexity Analysis

### Time Complexity: O(n²)

* Outer loop runs from 1 to n.
* Inner loop runs from 1 to `nodes`.
* Total operations ≈ n × n = O(n²)

This is efficient enough for n ≤ 19.

---

### Space Complexity: O(n)

* We use a DP array of size `n + 1`.
* No extra recursion stack or large data structures.

---

### Most Optimal Solution

This **Dynamic Programming solution is the optimal approach** for this problem because:

* A brute force approach would generate all possible trees and is computationally infeasible.
* This DP solution avoids redundant calculations.
* It reuses previously computed values efficiently.
* It runs in polynomial time and uses minimal extra memory.

---

## 5. Test Cases

```python
# Test Case 1:
n = 3
sol = Solution()
print(sol.numTrees(n))  # Output: 5

# Test Case 2:
n = 1
sol = Solution()
print(sol.numTrees(n))  # Output: 1
```