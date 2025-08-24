# [1493. Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=daily-question&envId=2025-08-24)

Given a binary array `nums`, you should delete one element from it.

Return the size of the longest non-empty subarray containing only `1`s in the resulting array.  
Return `0` if there is no such subarray.

---

## Examples

**Example 1:**

```
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
```

**Example 2:**

```
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
```

**Example 3:**

```
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
```

---

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

---

## Approach

We use the **sliding window** technique:

1. Keep two pointers `l` and `r` to represent the current window.  
2. Maintain a count of zeros in the window. We can allow **at most one zero** since we must delete one element.  
3. If the window contains more than one zero, move the left pointer `l` until only one zero remains.  
4. Track the maximum length of valid subarray (`r - l - 1`). The `-1` accounts for the deleted element.  
5. At the end, return the maximum of stored result and the last window length.

---

## Complexity Analysis

- **Time Complexity:** `O(n)` → Each element is visited at most twice (once by `r` and once by `l`).  
- **Space Complexity:** `O(1)` → Only a few variables are used.  

