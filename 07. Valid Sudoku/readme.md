# Valid Sudoku - LeetCode Blind 75

## Problem Statement
You are given a 9x9 Sudoku board represented as a 2D list. A Sudoku board is considered **valid** if it satisfies the following rules:

1. Each row must contain the digits 1-9 **without duplicates**.
2. Each column must contain the digits 1-9 **without duplicates**.
3. Each of the nine 3x3 sub-boxes (grids) must contain the digits 1-9 **without duplicates**.

The board may contain empty cells, denoted by the character `'.'`. The board does not need to be solvable or completely filled—only that the current state is valid.

### Example 1:
```python
Input:
board = [["1","2",".",".","3",".",".",".","."],
         ["4",".",".","5",".",".",".",".","."],
         [".","9","8",".",".",".",".",".","3"],
         ["5",".",".",".","6",".",".",".","4"],
         [".",".",".","8",".","3",".",".","5"],
         ["7",".",".",".","2",".",".",".","6"],
         [".",".",".",".",".",".","2",".","."],
         [".",".",".","4","1","9",".",".","8"],
         [".",".",".",".","8",".",".","7","9"]]

Output: True
```

### Example 2:
```python
Input:
board = [["1","2",".",".","3",".",".",".","."],
         ["4",".",".","5",".",".",".",".","."],
         [".","9","1",".",".",".",".",".","3"],
         ["5",".",".",".","6",".",".",".","4"],
         [".",".",".","8",".","3",".",".","5"],
         ["7",".",".",".","2",".",".",".","6"],
         [".",".",".",".",".",".","2",".","."],
         [".",".",".","4","1","9",".",".","8"],
         [".",".",".",".","8",".",".","7","9"]]

Output: False
Explanation: The number '1' appears twice in the top-left 3x3 sub-box.
```

---

## Approach: HashSet-Based Validation

### Key Insight
To validate a Sudoku board efficiently, we need to track seen numbers in:
- Each **row**
- Each **column**
- Each **3x3 sub-box**

We can use `defaultdict(set)` from Python's `collections` module to store seen values for each of the above. The `(r // 3, c // 3)` index will help identify each 3x3 sub-box.

### Code Explanation
```python
from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)     # Tracks seen numbers in each column
        rows = defaultdict(set)     # Tracks seen numbers in each row
        squares = defaultdict(set)  # Tracks seen numbers in each 3x3 grid

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # If the number already exists in the row, column, or square, it's invalid
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                # Otherwise, add the number to respective row, column, and square sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
```

---

## Time and Space Complexity

### Time Complexity: `O(n²)`
- We loop through each cell of the 9x9 board → total of 81 cells → O(81) → Generalized as O(n²) for an n x n board
- Each set lookup and insert is O(1) on average

### Space Complexity: `O(n²)`
- We maintain:
  - One set per row (9 rows)
  - One set per column (9 columns)
  - One set per square (9 squares)
- Worst case: All cells are filled with unique digits → each set holds up to 9 entries → Total auxiliary space is still proportional to O(n²)


---

## Conclusion
This is the most optimal and cleanest solution to the **Valid Sudoku** problem. It uses hash sets (via `defaultdict`) to track and validate constraints efficiently. This technique ensures that each number is unique within its row, column, and 3x3 box, and short-circuits the check as soon as a duplicate is found.

This problem is a classic in the Blind 75 list and is excellent for practicing set-based lookups and 2D traversal logic.
