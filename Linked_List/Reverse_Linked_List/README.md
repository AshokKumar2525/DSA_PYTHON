# [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)

## Problem Statement
Given the `head` of a singly linked list, reverse the list and return the reversed list.  

---

## Examples

**Example 1:**

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg" width="400">

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg" width="200">

```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**
```
Input: head = []
Output: []
```


---

## Constraints
- Number of nodes in the list: **[0, 5000]**  
- `-5000 <= Node.val <= 5000`  

**Follow-up:** A linked list can be reversed either **iteratively** or **recursively**.  

---

## Approach

### Iterative Approach (Implemented ✅)
1. Initialize three pointers:  
   - `pre = None`  
   - `cur = head`  
   - `post = head.next`  
2. Traverse the list while `post` is not null:  
   - Reverse the link (`cur.next = pre`).  
   - Move pointers one step forward (`pre, cur, post = cur, post, post.next`).  
3. At the end, link the last node (`cur.next = pre`) and return `cur` (new head).  

---

## Complexity Analysis
- **Time Complexity:** `O(n)` — Each node is visited once.  
- **Space Complexity:** `O(1)` — Only uses a constant number of pointers.  