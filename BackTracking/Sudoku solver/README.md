# 🧩 [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/description/)

## 📌 Problem Statement
Write a program to solve a **Sudoku puzzle** by filling the empty cells.

A sudoku solution must satisfy **all of the following rules** :

- ✅ Each of the digits `1-9` must occur exactly once in each **row**.  
- ✅ Each of the digits `1-9` must occur exactly once in each **column**.  
- ✅ Each of the digits `1-9` must occur exactly once in each of the 9 **3x3 sub-boxes** of the grid.  

The `'.'` character indicates **empty cells**.

---

## 🎯 Example
### Input  
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" style="height: 250px; width: 250px;">

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

## 📌 Constraints

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j] is a digit or '.'.`
#### ✅ It is guaranteed that the input board has only one solution.

---
## 🛠️ Approach (Step by Step)

We use **Backtracking with constraint tracking:**
1. Identify Constraints
    - Each row, column, and 3x3 box must contain digits 1–9 exactly once.
    - Use boolean arrays (row_used, col_used, box_used) to track already used numbers.
2. Preprocessing
    - Traverse the board.
    - Mark filled numbers as used in their row, column, and box.
    - Collect positions of blanks ('.').
3. Recursive Backtracking
    - Pick the next blank cell.
    - Try placing digits 1–9.
    - If the digit is not used in the row, column, or box → place it.
    - Recurse to fill the next blank.
    - If no number fits → backtrack (undo move).
4. Termination
    - When all blanks are filled, the board is solved.

⚡ This ensures that we **prune invalid states early**, making the solution efficient.

---

## 🚀 Complexity Analysis
### Time Complexity:
- Worst-case is exponential (since backtracking tries digits in blanks).
- But with pruning & constraints, it works efficiently for 9x9 Sudoku.

### Space Complexity:
- O(81 + 9*10*3) = constant space (board size fixed at 9x9).

---
