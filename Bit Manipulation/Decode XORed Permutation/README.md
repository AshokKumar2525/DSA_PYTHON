# [1734. Decode XORed Permutation](https://leetcode.com/problems/decode-xored-permutation/description/)

## Problem Statement
There is an integer array `perm` that is a permutation of the first `n` positive integers, where `n` is always **odd**.

It was encoded into another integer array `encoded` of length `n - 1`, such that:

```
encoded[i] = perm[i] XOR perm[i + 1]
```

For example, if `perm = [1,3,2]`, then `encoded = [2,1]`.

Given the `encoded` array, return the original array `perm`.  
It is guaranteed that the answer exists and is unique.

---

## Examples

**Example 1:**
```
Input: encoded = [3,1]
Output: [1,2,3]
Explanation: If perm = [1,2,3], then encoded = [1 XOR 2, 2 XOR 3] = [3,1]
```

**Example 2:**
```
Input: encoded = [6,5,4,6]
Output: [2,4,1,5,3]
```

---

## Constraints
- `3 <= n < 10^5`  
- `n` is odd.  
- `encoded.length == n - 1`  

---

## Approach


```text
1. Let `n = len(encoded) + 1` (since encoded is of size n-1).
2. Compute XOR of all numbers from 1 to n:
     total = 1 ^ 2 ^ ... ^ n
   Since `perm` is a permutation of 1 to n, this is also XOR of all elements of `perm`.

3. Compute XOR of all `encoded[i]` where i is odd (i.e., i = 1, 3, 5...):
     odd_xor = encoded[1] ^ encoded[3] ^ ...

   These correspond to `perm[1] ^ perm[2] ^ ... ^ perm[n-1]`
   (this is due to how the XOR pairs overlap in encoded).

4. Now, first element of perm can be obtained by:
     perm[0] = total ^ odd_xor

   Why? Because:
     total = perm[0] ^ perm[1] ^ ... ^ perm[n-1]
     odd_xor = perm[1] ^ ... ^ perm[n-1]
     => perm[0] = total ^ odd_xor

5. Once perm[0] is known, we can reconstruct the rest:
     perm[i+1] = perm[i] ^ encoded[i]

6. Return the reconstructed `perm` array.
```

---

## Complexity Analysis
- **Time Complexity:** `O(n)` → Each element is processed once.  
- **Space Complexity:** `O(1)` → Only uses a few extra variables (ignoring output list).  

---