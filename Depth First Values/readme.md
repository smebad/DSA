# Depth First Values - Binary Tree

## Introduction
A **binary tree** is a tree data structure where each node has at most two children, referred to as the left and right child. It is commonly used in various computing applications, including searching, sorting, and hierarchical data representation.

## What is Depth-First Traversal?
Depth-first traversal is a method for visiting all nodes in a binary tree. It explores as far as possible along each branch before backtracking. The traversal follows the pattern:
- Visit the root node
- Traverse the left subtree
- Traverse the right subtree

This approach ensures that we explore one branch completely before moving on to another.

## Solutions Implemented
### 1. Iterative Solution (Using a Stack)
This approach uses a **stack** (LIFO - Last In, First Out) to manually track the nodes to visit next.

#### Algorithm:
1. Initialize a stack with the root node.
2. While the stack is not empty:
   - Pop the top node from the stack.
   - Add its value to the result list.
   - Push its right child to the stack (if it exists).
   - Push its left child to the stack (if it exists).
3. Repeat until all nodes have been visited.

#### Time Complexity:
- **O(n)**, since each node is processed once.
- **Space Complexity:** O(n) in the worst case (for a completely unbalanced tree).

### 2. Recursive Solution
This approach uses **recursion** to traverse the tree in a depth-first manner.

#### Algorithm:
1. If the root is `None`, return an empty list.
2. Recursively call `depth_first_values` on the left subtree.
3. Recursively call `depth_first_values` on the right subtree.
4. Combine and return the results.

#### Time Complexity:
- **O(n²)** in the worst case, due to list concatenation (`*left_values, *right_values`).
- **Space Complexity:** O(n) for recursive call stack.

## Difference Between Iterative and Recursive Approaches
| Approach   | Time Complexity | Space Complexity | Advantage |
|------------|----------------|------------------|-------------|
| **Iterative (Stack)** | O(n) | O(n) | More efficient, avoids function call overhead |
| **Recursive** | O(n²) | O(n) | Cleaner code, easier to understand |

## Example Usage
```python
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.left = b
#a.right = c
#b.left = d
#b.right = e
#c.right = f

print(depth_first_values(a))  # ['a', 'b', 'd', 'e', 'c', 'f']
```

## Conclusion
- The **iterative solution** is more efficient in terms of time complexity.
- The **recursive solution** is more readable but can be inefficient due to list concatenation.
- Depth-first traversal is useful for exploring all nodes and can be applied to many real-world problems like pathfinding and expression trees.