# [2578. Split With Minimum Sum](https://leetcode.com/problems/split-with-minimum-sum/description/)

## 📌 Problem Statement
Given a positive integer `num`, split it into two non-negative integers `num1` and `num2` such that:

- The concatenation of `num1` and `num2` is a permutation of `num`.
- The sum of the number of occurrences of each digit in `num1` and `num2` is equal to the number of occurrences of that digit in `num`.
- `num1` and `num2` can contain leading zeros.  

Return the **minimum possible sum** of `num1` and `num2`.

🔹 **Notes:**  
- It is guaranteed that `num` does not contain any leading zeros.  
- The order of digits in `num1` and `num2` may differ from the order in `num`.  

---

## 📝 Examples  

**Example 1:**  
```
Input: num = 4325
Output: 59
Explanation: We can split 4325 so that num1 = 24 and num2 = 35, giving sum = 59.
```

**Example 2:**  
```
Input: num = 687
Output: 75
Explanation: We can split 687 so that num1 = 68 and num2 = 7, giving sum = 75.
```

---

## 🔒 Constraints
- `10 <= num <= 10^9`

---

## 💡 Approach (Step by Step)
1. Extract all digits of `num` and store them in a list.  
2. Sort the digits in ascending order.  
3. Distribute digits alternatively into two numbers (`num1` and `num2`).  
   - First digit goes to `num1`, second to `num2`, third to `num1`, and so on.  
   - This ensures digits are balanced and smaller digits contribute to a smaller sum.  
4. Convert `num1` and `num2` back into integers.  
5. Return the sum of `num1 + num2`.  

✅ This greedy approach ensures minimal possible sum.

---