# [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/)

**Companies:** Facebook, Amazon, Microsoft, Apple, Google  

---

## Problem Statement  
You are given an array of `k` linked-lists, each linked-list sorted in ascending order.  
Merge all the linked-lists into one sorted linked-list and return it.

---

## Examples  

**Example 1:**
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Explanation:
The linked-lists are:
[
1->4->5,
1->3->4,
2->6
]
Merged linked-list:
1->1->2->3->4->4->5->6
```

**Example 2:**
```
Input: lists = []
Output: []
```


**Example 3:**
```
Input: lists = [[]]
Output: []
```

---

## Constraints
- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- Each list is sorted in ascending order
- The sum of `lists[i].length` will not exceed `10^4`

---

## Approach  

We use a **min-heap (priority queue)** to efficiently merge the lists:

1. Push the first node of each non-empty list into a heap `(value, index, node)`.
   - The `index` ensures uniqueness when values are equal.
2. Pop the smallest node from the heap.
3. Append it to the merged result.
4. If the popped node has a next node, push it into the heap.
5. Repeat until the heap is empty.

This ensures nodes are always extracted in sorted order.

---

## Complexity Analysis  

- **Time Complexity:**  
  Each node is pushed and popped once → `O(N log k)`  
  where `N` = total number of nodes, `k` = number of lists  

- **Space Complexity:**  
  Heap stores at most `k` elements → `O(k)`  
