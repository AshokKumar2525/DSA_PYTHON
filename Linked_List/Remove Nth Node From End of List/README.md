# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=linked-list)

## Problem Statement  
Given the `head` of a linked list, remove the `n^th` node from the end of the list and return its head.

---

## Examples  

**Example 1:**
Input: `head = [1,2,3,4,5], n = 2`  
Output: `[1,2,3,5]`  

**Example 2:**  
Input: `head = [1], n = 1`  
Output: `[]`  

**Example 3:**  
Input: `head = [1,2], n = 1`  
Output: `[1]`  

---

## Constraints  
- The number of nodes in the list is `sz`.  
- `1 <= sz <= 30`  
- `0 <= Node.val <= 100`  
- `1 <= n <= sz`  

**Follow up:** Could you do this in one pass?

---

## Approach  

### (One-pass, Two Pointers)  
1. Use a dummy node pointing to the head to handle edge cases.  
2. Move the `fast` pointer `n+1` steps ahead to create a gap of `n` between `fast` and `slow`.  
3. Move both pointers until `fast` reaches the end.  
4. Now `slow` is right before the node to delete, so skip it using `slow.next = slow.next.next`.  
5. Return the modified list.  

✅ Handles edge cases like removing the head node.  
✅ One-pass solution.  

---

## Complexity Analysis  
- **Time Complexity:** `O(L)` where `L` is the length of the linked list.  
- **Space Complexity:** `O(1)` (no extra space used).  

---

## Alternative Approach (Two-pass)  
1. Find the length of the list.  
2. Calculate the index of the node to remove from the start (`length - n`).  
3. Traverse again and remove the node.  

- **Time Complexity:** `O(L)` (but requires 2 passes).  
- **Space Complexity:** `O(1)`.  

---

