# 🧩 Twisted Mirror Path Count  
**LeetCode Problem:** [3665. Twisted Mirror Path Count](https://leetcode.com/problems/twisted-mirror-path-count/description/)  

---

## 📌 Problem Statement  
You are given an `m x n` binary grid `grid` where:  
- `grid[i][j] == 0` → empty cell  
- `grid[i][j] == 1` → mirror  

A robot starts at `(0, 0)` and wants to reach `(m - 1, n - 1)`.  
- It can move **right** or **down**.  
- If it tries to move into a **mirror**:  
  - Moving **right → reflected down**  
  - Moving **down → reflected right**  
- If reflection pushes the robot **out of bounds**, that path is invalid.  
- Reflection is **continuous** if it enters another mirror.  

Return the **number of unique valid paths**, modulo `10^9 + 7`.  

---

## 🧪 Examples  

**Example 1**  
```text
Input: grid = [[0,1,0],[0,0,1],[1,0,0]]  
Output: 5
Explanation: There are 5 valid reflected paths to the bottom-right.
```
**Example 2**
```text
Input: grid = [[0,0],[0,0]]  
Output: 2
Explanation:
    Paths:
Right → Down
Down → Right
```
**Example 3**
```text
Input: grid = [[0,1,1],[1,1,0]]  
Output: 1
Explanation : Only one valid path exists due to reflections.
```
---

## 🎯 Constraints
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 500`
- `grid[i][j] ∈ {0, 1}`
- `grid[0][0] == grid[m-1][n-1] == 0`

## 🛠️ Approach (Step by Step)

We solve this using DP with state (r, c, dir) where dir indicates the direction of entry:
- 0 → entered from top (so robot came moving down)
- 1 → entered from left (so robot came moving right)

**Steps:
1. Base cases:
    - If (r, c) is outside grid → invalid.
    - If (r, c) is the destination (m-1, n-1) → valid path = 1.
2. When encountering a mirror (1):
    - If entered from top (dir=0) → must go right (dp(r, c+1, 1)).
    - If entered from left (dir=1) → must go down (dp(r+1, c, 0)).
3. When encountering empty cell (0):
    - Robot has both choices:
        - Go down → dp(r+1, c, 0)
        - Go right → dp(r, c+1, 1)
4. Memoization with @lru_cache to avoid recomputation.
5. Start from (0, 0) → we can go either down (1,0,0) or right (0,1,1) and sum the results.
---

## ⏱️ Complexity Analysis
- **Time Complexity:**
    - Each state is `(r, c, dir)` → `O(m * n * 2)`
    - Each state computed once due to memoization.
    - ✅ `O(m * n)`

- **Space Complexity:**
    - DP memoization table → `O(m * n * 2)`
    - Recursion depth up to `O(m+n)`
    - ✅ `O(m * n)`

---