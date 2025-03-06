# Zipper Lists

## Problem Statement
The **zipper_lists** function takes in the head nodes of two linked lists as arguments and combines them into a single linked list by alternating nodes from each list. If one list is longer than the other, the remaining nodes from the longer list should be appended at the end of the new linked list. The function modifies the input lists in-place and returns the head of the newly zippered linked list.

## Example
### Input:
```
List 1: a -> b -> c
List 2: x -> y -> z
```
### Output:
```
a -> x -> b -> y -> c -> z
```

---

## Solutions
### **1. Iterative Solution**

### **Approach:**
- Use a `tail` pointer initialized to `head_1`.
- Maintain two pointers: `current_1` (tracking the next node of `head_1`) and `current_2` (tracking the next node of `head_2`).
- Iterate through both lists while both have nodes remaining:
  - Append one node from `head_2`, then one node from `head_1` alternatively.
  - Move `tail` forward.
  - Continue until one of the lists is exhausted.
- If any list still has remaining nodes, append them to the tail.
- Return the head of `head_1`.

### **Code:**
```python
class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

def zipper_lists(head_1, head_2):
  if not head_1:
    return head_2
  if not head_2:
    return head_1

  tail = head_1
  current_1 = head_1.next
  current_2 = head_2
  count = 0

  while current_1 is not None and current_2 is not None:
    if count % 2 == 0:
      tail.next = current_2
      current_2 = current_2.next
    else:
      tail.next = current_1
      current_1 = current_1.next
    tail = tail.next
    count += 1

  if current_1 is not None:
    tail.next = current_1
  if current_2 is not None:
    tail.next = current_2

  return head_1
```

### **Time Complexity:**
- **O(n + m)**, where `n` is the length of `head_1` and `m` is the length of `head_2`.
- We iterate through all nodes of both lists at most once.

### **Space Complexity:**
- **O(1)**, as we modify the linked list in-place without additional data structures.

---

### **2. Recursive Solution**

### **Approach:**
- Base cases:
  - If both lists are empty, return `None`.
  - If `head_1` is empty, return `head_2`.
  - If `head_2` is empty, return `head_1`.
- Recur with the next nodes of both lists, swapping `head_1.next` with `head_2` at each step.
- Return `head_1` as the new head of the zippered list.

### **Code:**
```python
class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

def zipper_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None
  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1

  next_1 = head_1.next
  next_2 = head_2.next
  head_1.next = head_2
  head_2.next = zipper_lists(next_1, next_2)
  return head_1  
```

### **Time Complexity:**
- **O(n + m)**: The recursion traverses through the minimum of `n` and `m` elements.

### **Space Complexity:**
- **O(min(n, m))**: Since recursive calls are stored on the call stack, the maximum depth is limited by the smaller list.

---

## **Comparison of Iterative and Recursive Approaches**
| Solution  | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Iterative | O(n + m)       | O(1)             | Modifies list in-place efficiently |
| Recursive | O(n + m)       | O(min(n, m))     | Uses stack space for recursion |

### **Which One to Use?**
- **Use Iterative** if optimizing for space, as it runs in **O(1) space**.
- **Use Recursive** if you prefer a cleaner, elegant approach, but it may lead to **stack overflow** for very large lists.

---

## Conclusion
Both iterative and recursive approaches achieve the same goal, but iterative is more efficient in terms of space. Recursive is easier to read but may cause issues with deep recursion. Choose based on constraints and readability preferences.