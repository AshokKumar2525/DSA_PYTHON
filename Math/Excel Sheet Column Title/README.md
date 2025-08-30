# 📊 [168. Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/description/)

---

## 🏢 Companies Asked:
<p align="left">
  <img src="https://logo.clearbit.com/microsoft.com" width="18px" style="margin-right:5px;"/> Microsoft  
  <img src="https://logo.clearbit.com/google.com" width="18px" style="margin-right:5px;"/> Google  
  <img src="https://logo.clearbit.com/amazon.com" width="18px" style="margin-right:5px;"/> Amazon  
</p>

---

## 💡 Problem Statement

Given an integer `columnNumber`, return its corresponding column title as it appears in an Excel sheet.

For example:
```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
```

---

## 📝 Examples

**Example 1:**  
```
Input: columnNumber = 1
Output: "A"
```

**Example 2:**
```  
Input: columnNumber = 28
Output: "AB"
```

**Example 3:**  
```
Input: columnNumber = 701
Output: "ZY"
```

---

## 📌 Constraints
- `1 <= columnNumber <= 2^31 - 1`

---

## 🚀 Approach (Step by Step)
1. Think of this as **base-26 conversion**, similar to how numbers are converted to binary or hex.  
2. Excel columns are **1-indexed** (i.e., A = 1, not 0), so we subtract `1` at every step.  
3. Get the last character by doing `columnNumber % 26`.  
   - Add it to the result string.  
4. Divide `columnNumber` by 26 and continue until it becomes 0.  
5. Reverse the constructed string since we build it backwards.

---