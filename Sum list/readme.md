# Sum List - Linked List Sum Calculation

## Overview
The **Sum List** problem requires computing the total sum of all values in a linked list. Given the head of a linked list containing numbers, we traverse through the list and return the sum of all node values.

We implemented two solutions:
1. **Iterative Approach** (Efficient in terms of space complexity)
2. **Recursive Approach** (Simpler but uses more memory)

---

## Iterative Approach
### Explanation
In the iterative solution, we initialize a `total_sum` variable and traverse through the linked list using a loop, adding each node's value to `total_sum`. The function returns the final computed sum.

### Code:
```python
def sum_list(head):
    total_sum = 0
    current = head
    while current is not None:
        total_sum += current.val
        current = current.next
    return total_sum
```

### Complexity Analysis:
- **Time Complexity:** O(n) - We iterate through all `n` nodes once.
- **Space Complexity:** O(1) - We only use a single variable (`total_sum`), independent of input size.

---

## Recursive Approach
### Explanation
In the recursive solution, we break the problem down into smaller parts:
- **Base case:** If `head` is `None`, return `0`.
- Otherwise, return the value of the current node plus the sum of the remaining list.

### Code:
```python
def sum_list(head):
    if head is None:
        return 0
    return head.val + sum_list(head.next)
```

### Complexity Analysis:
- **Time Complexity:** O(n) - We visit each node once.
- **Space Complexity:** O(n) - Due to recursive function calls, the call stack stores `n` function calls.

---

## Choosing the Best Approach
| Approach  | Time Complexity | Space Complexity | Best Use Case |
|-----------|---------------|----------------|--------------|
| Iterative | O(n)          | O(1)           | Best for large lists where memory optimization is needed |
| Recursive | O(n)          | O(n)           | More elegant and concise, but consumes more memory |

- **Use iterative** when working with very large linked lists to avoid stack overflow.
- **Use recursive** for a simpler implementation if memory constraints are not an issue.

---

## Test Cases
### Example 1:
**Input:**  
`2 -> 8 -> 3 -> -1 -> 7`  
**Output:**  
`19`

### Example 2:
**Input:**  
`38 -> 4`  
**Output:**  
`42`

### Example 3:
**Input:**  
`100`  
**Output:**  
`100`

### Example 4:
**Input:**  
`None` (Empty List)  
**Output:**  
`0`

---

## Conclusion
This problem demonstrates how linked list traversal can be performed both iteratively and recursively. The choice between these two depends on the constraints and requirements of the problem.