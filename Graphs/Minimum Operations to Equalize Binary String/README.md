# 🚀 Minimum Operations to Equalize Binary String  

## 📌 Problem Statement  
You are given a binary string `s`, and an integer `k`.  

In **one operation**, you must choose exactly `k` different indices and **flip** each character (`'0' → '1'` and `'1' → '0'`).  

Return the **minimum number of operations** required to make all characters in the string equal to `'1'`.  
If it is not possible, return **-1**.  

---

## 🔍 Examples  

### ✅ Example 1  
**Input:**  
```
s = "110", k = 1
```
**Output:**  
```
1
```
**Explanation:**  
- There is one `'0'`.  
- Since `k = 1`, we can flip it directly in one operation.  

---

### ✅ Example 2  
**Input:**  
```
s = "0101", k = 3
```
**Output:**  
```
2
```
**Explanation:**  
- Operation 1: Flip indices `[0, 1, 3]` → `"1000"`  
- Operation 2: Flip indices `[1, 2, 3]` → `"1111"`  
- **Minimum operations = 2**  

---

### ✅ Example 3  
**Input:**  
```
s = "101", k = 2
```
**Output:**  
```
-1
```
**Explanation:**  
- Only one `'0'`, but we must flip **2 indices** at a time.  
- **Impossible**, so answer = -1.  

---

## ⚙️ Constraints  
- `1 <= s.length <= 10^5`  
- `s[i]` is either `'0'` or `'1'`.  
- `1 <= k <= s.length`  

---

## 🧠 Approach  

We treat the problem as a **graph shortest path problem (BFS)**:  

1. Let `a0 = number of zeros` in `s`.  
   - If `a0 == 0` → Already all `'1'` → Return `0`.  

2. Each state is defined by the **number of zeros (`a`)** in the string.  
   - Range: `0 <= a <= n`.  

3. From a state `a`, if we flip `x` zeros and `(k-x)` ones:  
   - New zero count = `a' = a + k - 2*x`  
   - Valid if `0 <= a' <= n`.  

4. Since `a'` and `a` must have the same **parity relation** (`(a+k) % 2`),  
   we separate states into **even** and **odd buckets** for efficiency.  

5. Use **BFS (queue + sorted sets)** to explore reachable states.  
   - First time we reach `a = 0`, return number of operations.  

6. If no valid path exists → return `-1`.  

---
## ⏱️ Time & Space Complexity
- **Time Complexity:**
    - Each state (number of zeros) is processed once.
    - Each bucket operation is `O(log n)`.
    - Worst-case: `O(n log n)`
- **Space Complexity:**
    - Distance array `O(n)`
    - Two buckets storing states `O(n)`
    - BFS queue `O(n)`
    - Overall: `O(n)`