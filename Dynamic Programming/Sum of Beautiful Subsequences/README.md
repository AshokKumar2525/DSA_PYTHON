# [3671. Sum of Beautiful Subsequences](https://leetcode.com/problems/sum-of-beautiful-subsequences/description/)

## 📌 Problem Statement
You are given an integer array `nums` of length `n`.

For every **positive integer** `g`, we define the **beauty** of `g` as the **product** of `g` and the number of **strictly increasing subsequences** of `nums` whose greatest common divisor (GCD) is exactly `g`.

Return the **sum of beauty values** for all positive integers `g`.

Since the answer could be very large, return it modulo `10^9 + 7`.

---

## ✨ Examples

### Example 1
**Input:**
```
nums = [1, 2, 3]
```
**Output:**
```
10
```

**Explanation:**  
Strictly increasing subsequences and their GCDs:

| Subsequence | GCD |
|-------------|-----|
| [1]         | 1   |
| [2]         | 2   |
| [3]         | 3   |
| [1,2]       | 1   |
| [1,3]       | 1   |
| [2,3]       | 1   |
| [1,2,3]     | 1   |

- GCD = 1 → 5 subsequences → Beauty = `1 × 5 = 5`  
- GCD = 2 → 1 subsequence → Beauty = `2 × 1 = 2`  
- GCD = 3 → 1 subsequence → Beauty = `3 × 1 = 3`  

✅ Total beauty = `5 + 2 + 3 = 10`

---

### Example 2
**Input:**
```
nums = [4, 6]
```
**Output:**
```
12
```

**Explanation:**  
Strictly increasing subsequences and their GCDs:

| Subsequence | GCD |
|-------------|-----|
| [4]         | 4   |
| [6]         | 6   |
| [4,6]       | 2   |

- GCD = 2 → Beauty = `2 × 1 = 2`  
- GCD = 4 → Beauty = `4 × 1 = 4`  
- GCD = 6 → Beauty = `6 × 1 = 6`  

✅ Total beauty = `2 + 4 + 6 = 12`

---

## 🔒 Constraints
- `1 <= n == nums.length <= 10^4`  
- `1 <= nums[i] <= 7 * 10^4`  

---

## 💡 Approach

1. **Observation**  
   - Each subsequence contributes to exactly one GCD value.  
   - For every possible `g`, we must count subsequences with `gcd = g`.  

2. **Steps**
   - Precompute divisors of numbers in `nums`.  
   - For each divisor `d`, build a subsequence array scaled by `d`.  
   - Count **strictly increasing subsequences** using **Fenwick Tree (BIT)**.  
   - Apply **Möbius inversion** to separate counts of subsequences with exact GCD = `g`.  

3. **Final Computation**  
   - For each `g`, calculate `beauty = g × count(g)`  
   - Sum over all valid `g` modulo `10^9 + 7`.

---

## 🧮 Complexity Analysis
- **Time Complexity:**  
  - ~`O(max(nums) log(max(nums)) + n log(max(nums)))` due to Fenwick Tree and divisor iteration.  
  - Efficient for `n ≤ 10^4` and `nums[i] ≤ 7e4`.

- **Space Complexity:**  
  - `O(max(nums))` for Möbius, Fenwick Tree, divisor storage.

---