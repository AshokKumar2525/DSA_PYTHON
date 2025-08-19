# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

## Problem Statement
You are given two **non-empty linked lists** representing two non-negative integers.  
The digits are stored in **reverse order**, and each of their nodes contains a single digit.  
Add the two numbers and return the sum as a linked list.  

You may assume the two numbers do not contain any leading zeros, except the number `0` itself.  

---

## Examples

**Example 1:**
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" width="400">

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
```

**Example 2:**
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:**
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```


---


---

## Constraints
- Number of nodes in each linked list: **[1, 100]**  
- `0 <= Node.val <= 9`  
- Guaranteed that the list represents a number without leading zeros  

---

## Approach

1. Use a **dummy head** node to simplify linked list construction.  
2. Initialize a **carry = 0**.  
3. Traverse both lists simultaneously:  
   - Extract values `l1Val` and `l2Val` (default to `0` if the list is exhausted).  
   - Compute `columnSum = l1Val + l2Val + carry`.  
   - Update `carry = columnSum // 10`.  
   - Create a new node with value `columnSum % 10` and attach it to the result.  
4. Continue until both lists and carry are exhausted.  
5. Return `dummy.next` (skipping the dummy head).  

---

## Complexity Analysis
- **Time Complexity:** `O(max(m, n))`  
  - Each node in both lists is processed once.  
- **Space Complexity:** `O(max(m, n))`  
  - Output list has at most one extra node than the longer input list.  

---

## Other Possible Approaches
**Direct Addition Without Reversing:**
Iterate over the lists directly as given (reverse order), maintaining carry.

**Stack-Based Solution:**
Push values from both lists into stacks, pop and add to simulate manual addition.