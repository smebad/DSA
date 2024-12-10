# Intersection Problem

## Introduction

The **Intersection Problem** involves finding common elements between two lists. The task is to implement a function `intersection` that takes in two lists, `a` and `b`, as inputs and returns a new list containing elements that exist in both lists.

### Assumptions
- Each input list does not contain duplicate elements.

---

## Solutions

We will implement two solutions to the problem: a **brute-force solution** and an **optimized solution using sets**.

---

### 1. Brute-Force Solution

In the brute-force solution, we iterate through each element of `b` and check if it exists in `a`. If it does, we add it to the result list.

#### Implementation
```python
def intersection(a, b):
    result = []
    for item in b:
        if item in a:
            result.append(item)
    return result
```

### Time Complexity

- **Time:** O(n * m), where `n` is the length of `a` and `m` is the length of `b`. This is because for each element in `b`, we search through `a`, which takes linear time.
- **Space:** O(min(n, m)), as the result list stores common elements.

#### Limitations
The brute-force solution becomes inefficient for large inputs due to its high time complexity.


### 2. Optimized Solution Using Sets

To improve efficiency, we convert a into a set. Checking membership in a set is faster (O(1) on average), allowing us to achieve better performance.

#### Implementation
``` python
def intersection(a, b):
    set_a = set(a)
    return [item for item in b if item in set_a]
```
### Time Complexity

- **Time:** O(n + m)
  - Converting `a` to a set takes O(n).
  - Iterating through `b` and checking membership in `set_a` takes O(m).
- **Space:** O(n), as we store all elements of `a` in a set.

#### Advantages
This approach is significantly faster and more scalable for large lists.

---

### Comparison of Solutions

| **Aspect**          | **Brute-Force Solution** | **Optimized Solution (Set)** |
|----------------------|--------------------------|------------------------------|
| **Time Complexity**  | O(n * m)                | O(n + m)                    |
| **Space Complexity** | O(min(n, m))            | O(n)                        |
| **Scalability**      | Poor                    | Excellent                   |

---

### Conclusion

- The **brute-force solution** is simple but inefficient for large inputs.
- The **optimized solution using sets** provides significant performance gains and should be preferred for practical applications.
