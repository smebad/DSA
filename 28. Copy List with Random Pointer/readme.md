# Copy List with Random Pointer - LeetCode

## Problem Description

You are given a special type of singly linked list where each node contains two pointers:
- `next`: Points to the next node in the list.
- `random`: Can point to any node in the list or be `null`.

The task is to **create a deep copy** of this list. A deep copy means that all nodes must be newly created, with the same `val` values and correctly replicated `next` and `random` pointer structure. The new nodes must not share memory addresses with the original ones.

### Example

**Input:**
```
head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
```
**Output:**
```
[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

The structure and `random` connections must be identical but with new node instances.

---

## Python Solution: HashMap + Two-Pass

This solution uses a dictionary to map original nodes to their copies in two separate passes.

```python
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Dictionary to map original nodes to their copies
        oldToCopy = {None: None}  # Initialize with None to handle null pointers

        # First pass: Copy nodes and store mapping from original to copy
        cur = head
        while cur:
            copy = Node(cur.val)  # Create a copy of the current node
            oldToCopy[cur] = copy
            cur = cur.next

        # Second pass: Assign next and random pointers to the copied nodes
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]     # Link the next pointer
            copy.random = oldToCopy[cur.random] # Link the random pointer
            cur = cur.next

        # Return the head of the copied list
        return oldToCopy[head]
```

### Explanation
1. **HashMap Initialization:** We start by initializing a dictionary `oldToCopy` with `{None: None}` to simplify null pointer checks.
2. **First Loop:** We iterate through the original list and for each node, we create a copy with the same value and store the original-to-copy mapping.
3. **Second Loop:** We again iterate through the original list. For each node, we use the dictionary to assign:
   - `copy.next` to the copy of the original's `next`
   - `copy.random` to the copy of the original's `random`
4. **Return:** Finally, we return the copied version of the original `head` using `oldToCopy[head]`.

---

## Time and Space Complexity

### Time Complexity: `O(n)`
- We make two passes through the original list (each of `O(n)` time).
- All dictionary operations are `O(1)`.

### Space Complexity: `O(n)`
- We use a dictionary to store mappings from original to copied nodes.
- Each original node is stored once, resulting in `O(n)` additional space.

---

## Why This is the Optimal Solution

While there is a method to reduce space to `O(1)` by weaving and unweaving the list, it requires modifying the original structure temporarily. However, this HashMap-based two-pass solution:
- Is easier to implement.
- Avoids modifying the input.
- Offers clarity and maintainability.

Thus, it is the most optimal solution **in terms of simplicity and readability** while maintaining linear time and space.

---

## Test Case Utility Functions

To test the solution, the following helper functions are used:

```python
# Build a linked list with random pointers from input data
def build_linked_list(data):
    if not data:
        return None
    nodes = [Node(val) for val, _ in data]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_, rand_idx) in enumerate(data):
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]

# Serialize the copied linked list back to the input format
def serialize_linked_list(head):
    result = []
    node_to_index = {}
    cur = head
    idx = 0
    while cur:
        node_to_index[cur] = idx
        cur = cur.next
        idx += 1
    cur = head
    while cur:
        rand_idx = node_to_index[cur.random] if cur.random else None
        result.append([cur.val, rand_idx])
        cur = cur.next
    return result
```

---

## Test Cases

```python
def test(input_data):
    print("Input:", input_data)
    head = build_linked_list(input_data)
    copied_head = Solution().copyRandomList(head)
    output = serialize_linked_list(copied_head)
    print("Copied:", output)
    print("-" * 40)

test([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
test([[1, 1], [2, 1]])
test([[3, None], [3, 0], [3, None]])
```

