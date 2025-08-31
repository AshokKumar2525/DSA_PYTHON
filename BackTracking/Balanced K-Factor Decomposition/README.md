# Balanced K-Factor Decomposition

[LeetCode Problem 3669](https://leetcode.com/problems/balanced-k-factor-decomposition/description/)

## Problem Statement
Given two integers `n` and `k`, split the number `n` into exactly `k` positive integers such that the **product** of these integers is equal to `n`.

Return any one split in which the **maximum difference** between any two numbers is **minimized**.  
You may return the result in any order.

### Example 1
**Input:**  
```
n = 100, k = 2
```
**Output:**  
```
[10, 10]
```
**Explanation:**  
The split `[10, 10]` yields `10 * 10 = 100` and a max-min difference of `0`, which is minimal.

---

### Example 2
**Input:**  
```
n = 44, k = 3
```
**Output:**  
```
[2, 2, 11]
```
**Explanation:**  
Possible splits:  
- `[1, 1, 44]` → difference = 43  
- `[1, 2, 22]` → difference = 21  
- `[1, 4, 11]` → difference = 10  
- `[2, 2, 11]` → difference = 9 ✅ (minimal)

---

## Constraints
- `4 <= n <= 10^5`  
- `2 <= k <= 5`  
- `k` is strictly less than the total number of positive divisors of `n`.

---

## Approach

1. **Prime Factorization:**  
   Break `n` into prime factors.

2. **Backtracking / DFS Distribution:**  
   Distribute prime factors across `k` groups. Each group’s product contributes to the final split.

3. **Optimization with Pruning:**  
   - Track the remaining product to compute a best-possible bound.  
   - Skip states that cannot improve the current best difference.  
   - Use memoization (`seen` states) to avoid recomputation.

4. **Result:**  
   Return the split with the minimal max-min difference.

---

## Topics
- Math / Number Theory (Prime Factorization, Divisors)  
- Backtracking / DFS (Search for optimal grouping)  
- Greedy + Optimization (Minimize difference)  
- Search + Pruning (State caching, bounds)

---

## Complexity Analysis
- **Time Complexity:**  
  `O(k^m)` in the worst case, where `m` is the number of prime factors of `n`.  
  With pruning + memoization, it runs efficiently since `k <= 5` and `n <= 1e5`.

- **Space Complexity:**  
  `O(m + k)` for recursion stack and group storage.  
  Extra space for memoization set.

---
