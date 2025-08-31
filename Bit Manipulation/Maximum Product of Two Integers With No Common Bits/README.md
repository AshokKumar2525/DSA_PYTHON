# 🧩 Maximum Product of Two Integers With No Common Bits  
**LeetCode Problem:** [3670. Maximum Product of Two Integers With No Common Bits](https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/description/)  

---

## 📌 Problem Statement  
You are given an integer array `nums`.  

Your task is to find two **distinct** indices `i` and `j` such that the product `nums[i] * nums[j]` is **maximized**, and the **binary representations** of `nums[i]` and `nums[j]` do not share any **common set bits**.  

- Return the **maximum** possible product of such a pair.  
- If no such pair exists, return `0`.  

---

## 🧪 Examples  

**Example 1**  
```text
Input: nums = [1,2,3,4,5,6,7]  
Output: 12  
Explanation:  
Best pair = (3 -> 011, 4 -> 100).  
They share no set bits, so product = 3 × 4 = 12.
```
**Example 2**
```
Input: nums = [5,6,4]  
Output: 0  
Explanation:  
All pairs share common bits → no valid pair.  
```
**Example 3**
```
Input: nums = [64,8,32]  
Output: 2048  
Explanation:  
64 (1000000) and 32 (0100000) share no bits → product = 2048.  
```
---

## 🎯 Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

---
## 🚀 Approach
- **Observation**: Two numbers are valid if their bitwise AND = 0.
- **Idea**: Precompute the best (largest) number for every bitmask.
- **Subset Propagation**: Use SOS DP (Sum Over Subsets DP) to fill best values.
- **Final Answer**: For each number, find its partner using full_mask ^ num.
---

## ⏱️ Time and Space Complexity
- **Time Complexity:**
    - Precomputing best values: O(n)
    - Subset DP propagation: O(B * 2^B) where B = 20
    - Final scan of nums: O(n)
    - Total: O(n + B * 2^B) ≈ O(n + 20 * 2^20) → Efficient for given constraints.

- **Space Complexity:**
    - best array of size 2^B → O(2^B)
    - No extra heavy data structures.
    - Total: O(2^B + n) → about 10^6 + n, feasible.