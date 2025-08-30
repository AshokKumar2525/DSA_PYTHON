# ✅ 36. Valid Sudoku  

> [LeetCode Problem Link](https://leetcode.com/problems/valid-sudoku/description/?envType=daily-question&envId=2025-08-30)  

---

## 📝 Problem Statement  

Determine if a **9 x 9 Sudoku board** is valid. Only the filled cells need to be validated according to the following rules:  

- Each **row** must contain the digits `1-9` **without repetition**.  
- Each **column** must contain the digits `1-9` **without repetition**.  
- Each of the nine **3 x 3 sub-boxes** of the grid must contain the digits `1-9` **without repetition**.  

⚠️ **Note:**  
- A Sudoku board (partially filled) could be valid but not necessarily solvable.  
- Only filled cells need validation.  

---

## 📊 Examples  

### Example 1:  

**Input:**  
```
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```

**Output:**  
```
true
```

---

### Example 2:  

**Input:**  
```
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```

**Output:**  
```
false
```

**Explanation:** Two `8`s exist in the top-left 3×3 sub-box → Invalid.  

---

## 🚀 Approach  

We need to validate **rows, columns, and boxes** simultaneously while iterating over the board.  

### Step-by-Step:  
1. Create three lists of sets:  
   - `rows[9]`: store seen numbers for each row.  
   - `cols[9]`: store seen numbers for each column.  
   - `boxes[9]`: store seen numbers for each 3×3 sub-box.  

2. Traverse each cell `(i, j)` in the board:  
   - If the cell is `.`, skip.  
   - Compute the box index as `(i // 3) * 3 + (j // 3)`.  
   - If the number already exists in `rows[i]`, `cols[j]`, or `boxes[box]` → return `False`.  
   - Otherwise, add the number to the respective sets.  

3. If no violations are found, return `True`.  

---

## ⏱️ Complexity Analysis  

- **Time Complexity:** `O(9 × 9) = O(81)` → constant time since board size is fixed.  
- **Space Complexity:** `O(9 + 9 + 9) = O(27)` → constant space for sets.  

---
