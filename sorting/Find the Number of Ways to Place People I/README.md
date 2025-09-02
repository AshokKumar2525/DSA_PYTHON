# 🧩 LeetCode 3025. Find the Number of Ways to Place People I

---

## 📌 Problem Statement
You are given a 2D array `points` of size `n x 2` representing integer coordinates of some points on a 2D plane, where `points[i] = [xi, yi]`.

Count the number of pairs of points `(A, B)`, where:

- `A` is on the **upper-left** side of `B`:
  - `A.x <= B.x`
  - `A.y >= B.y`
- The rectangle (or line) they form has **no other points** inside or on its border.

Return the total count.

---

## 🔍 Examples

### Example 1
```
Input: points = [[1,1],[2,2],[3,3]]
Output: 0
```

### Example 2
```
Input: points = [[6,2],[4,4],[2,6]]
Output: 2
```

### Example 3
```
Input: points = [[3,1],[1,3],[1,1]]
Output: 2
```

---

## ✅ Constraints
- `2 <= n <= 50`
- `points[i].length == 2`
- `0 <= points[i][0], points[i][1] <= 50`
- All `points[i]` are distinct

---

## 💡 Approach

### Key Ideas
1. A valid pair `(A, B)` must satisfy:
   - `xA <= xB` and `yA >= yB`
   - No third point lies in the rectangle `[xA, xB] × [yB, yA]`.

2. **Naive method**: For every pair `(A, B)`, scan all other points to check emptiness → `O(n³)`.

3. **Optimized method**:
   - Sort points by `(x ascending, y descending)`.
   - For each point `A`, sweep rightward over candidates `B`.
   - Maintain `candidate_y = -1`, which tracks the lowest valid `y` so far.
   - If `yB <= yA` and `yB > candidate_y`, then `(A, B)` is valid.
   - Update `candidate_y = yB`.

This works because once a point at some `y` is paired, any deeper point is blocked.

---

## ⏱️ Complexity Analysis
- Sorting: `O(n log n)`
- Nested loops: `O(n²)`
- **Total complexity: O(n²)** (optimal, since up to Θ(n²) valid pairs may exist)
- Extra space: `O(1)`
