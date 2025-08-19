# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

## Problem Statement
You are given two **non-empty linked lists** representing two non-negative integers.  
The digits are stored in **reverse order**, and each of their nodes contains a single digit.  
Add the two numbers and return the sum as a linked list.  

You may assume the two numbers do not contain any leading zeros, except the number `0` itself.  

---

## Examples

**Example 1:**
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

## Constraints
- Number of nodes in each linked list: **[1, 100]**  
- `0 <= Node.val <= 9`  
- Guaranteed no leading zeros in the number  

---

## My Approach
1. **Reverse the Lists First**  
   - Since the digits are stored in reverse order, I first reverse the lists using a helper function `reverseList`.  
   - After reversing, the most significant digit comes first, which makes the addition easier.  

2. **Digit-wise Addition with Carry**  
   - Traverse both lists simultaneously.  
   - For each pair of nodes, add their values along with any carry from the previous step.  
   - Create a new node for the result digit, and propagate the carry forward.  

3. **Handle Remaining Carry**  
   - If there is a carry left after processing all nodes, add a final node.  

4. **Reverse the Result (if needed)**  
   - Since the result may be built in forward order, I reverse the final list again to return the expected format.  

---

## Complexity Analysis
- **Time Complexity:** `O(max(m, n))`  
  - We traverse both linked lists once, where `m` and `n` are their lengths.  
- **Space Complexity:** `O(max(m, n))`  
  - Output list size is at most one node longer than the longer input list.  

---

## Other Possible Approaches
**Direct Addition Without Reversing:**
Iterate over the lists directly as given (reverse order), maintaining carry.

**Stack-Based Solution:**
Push values from both lists into stacks, pop and add to simulate manual addition.