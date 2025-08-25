# [498. Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse/description/?envType=daily-question&envId=2025-08-25)

## Problem Statement
Given an `m x n` matrix `mat`, return an array of all the elements of the array in a diagonal order.

---

## Examples

**Example 1:**
```

Input: mat = [[1,2,3],
[4,5,6],
[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
```

---

**Example 2:**

```
Input: mat = [[1,2],
[3,4]]
Output: [1,2,3,4]
```

---

## Constraints
- `m == mat.length`  
- `n == mat[i].length`  
- `1 <= m, n <= 10^4`  
- `1 <= m * n <= 10^4`  
- `-10^5 <= mat[i][j] <= 10^5`  

---

## Approach

1. Traverse all diagonals using `d` where `d` goes from `0` to `m+n-2`.  
2. For each diagonal, determine the starting point `(r, c)`:
   - If `d < m`: start at `(d, 0)`  
   - Else: start at `(m-1, d-m+1)`  
3. Collect elements along the diagonal until indices go out of bounds.  
4. Reverse every alternate diagonal (to match zig-zag traversal).  
5. Append elements into result list.  

---

## Complexity Analysis
- **Time Complexity:** `O(m * n)` → Every element is visited once.  
- **Space Complexity:** `O(1)` → Ignoring result storage.  

---