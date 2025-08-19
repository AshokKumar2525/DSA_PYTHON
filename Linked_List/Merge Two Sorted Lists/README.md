# [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)

## Problem Statement
You are given the heads of two sorted linked lists `list1` and `list2`.  

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.  

Return the head of the merged linked list.  

---

## Examples

**Example 1:**

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" width="500">

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```


**Example 2:**
```
Input: list1 = [], list2 = []
Output: []
```

**Example 3:**
```
Input: list1 = [], list2 = [0]
Output: [0]
```

---

## Constraints
- Number of nodes in both lists: **[0, 50]**  
- `-100 <= Node.val <= 100`  
- Both `list1` and `list2` are sorted in **non-decreasing order**  

---

## Approach

1. Use a **dummy head** node to simplify list construction.  
2. Maintain a `current` pointer starting from the dummy node.  
3. Traverse both lists while both have elements:  
   - Compare `list1.val` and `list2.val`.  
   - Append the smaller node to `current.next`.  
   - Move the pointer forward in the chosen list.  
4. Once one list is exhausted, link the remaining nodes of the other list.  
5. Return `dummy.next` as the head of the merged sorted list.  

---

## Complexity Analysis
- **Time Complexity:** `O(m + n)`  
  - Each node from both lists is processed exactly once.  
- **Space Complexity:** `O(1)`  
  - Only a few pointers are used, no extra space apart from the output list.  

---