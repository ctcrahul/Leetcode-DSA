<h2><a href="https://leetcode.com/problems/sudoku-solver">37. Sudoku Solver</a></h2><h3>Hard</h3><hr><p>Write a program to solve a Sudoku puzzle by filling the empty cells.</p>

**Difficulty:** Hard  

Write a program to solve a Sudoku puzzle by filling the empty cells.

A Sudoku solution must satisfy all of the following rules:

1. Each digit `1-9` must occur exactly once in each row.
2. Each digit `1-9` must occur exactly once in each column.
3. Each digit `1-9` must occur exactly once in each of the nine `3x3` sub-boxes of the grid.

The `'.'` character indicates empty cells.

---

##  Example

### Input

```python
board = [
 ["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]
```

### Output

```python
[
 ["5","3","4","6","7","8","9","1","2"],
 ["6","7","2","1","9","5","3","4","8"],
 ["1","9","8","3","4","2","5","6","7"],
 ["8","5","9","7","6","1","4","2","3"],
 ["4","2","6","8","5","3","7","9","1"],
 ["7","1","3","9","2","4","8","5","6"],
 ["9","6","1","5","3","7","2","8","4"],
 ["2","8","7","4","1","9","6","3","5"],
 ["3","4","5","2","8","6","1","7","9"]
]
```

---

##  Approach

We use the **Backtracking Algorithm**.

### Steps:

1. Traverse the board cell by cell.
2. If an empty cell (`'.'`) is found:
   - Try placing digits from `1` to `9`.
   - Check if the placement is valid.
   - If valid → place it and recurse.
   - If not valid → try next digit.
   - If no digit works → backtrack.
3. Continue until the board is completely filled.

---




---

##  Time Complexity

Worst case: `O(9^(n²))`

Backtracking explores possibilities but constraint checking reduces unnecessary recursion.

---

##📦 Space Complexity

- O(1) extra space (in-place modification)
- O(n²) recursion stack in worst case

---

##  Concepts Used

- Recursion
- Backtracking
- Matrix Traversal
- Constraint Validation
