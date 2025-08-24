# [31. Next Permutation](https://leetcode.com/problems/next-permutation/description/)

A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

- For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`:  
  `[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer.  
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

- Example:  
  - The next permutation of `arr = [1,2,3]` is `[1,3,2]`.  
  - The next permutation of `arr = [2,3,1]` is `[3,1,2]`.  
  - The next permutation of `arr = [3,2,1]` is `[1,2,3]`.  

The replacement must be **[in place](http://en.wikipedia.org/wiki/In-place_algorithm)** and use only constant extra memory.

---

## Examples

**Example 1:**  
```
Input: nums = [1,2,3]
Output: [1,3,2]
```

**Example 2:**  
```
Input: nums = [3,2,1]
Output: [1,2,3]
```

**Example 3:**  
```
Input: nums = [1,1,5]
Output: [1,5,1]
```


---

## Constraints
- `1 <= nums.length <= 100`  
- `0 <= nums[i] <= 100`  

---

## Approach

1. **Find the first decreasing element** (from right to left):  
   - Traverse the array from the end to find the first index `i` such that `nums[i] < nums[i+1]`.  
   - This identifies the "pivot" point where the next permutation change must occur.  

2. **Find the next larger element** (from right side):  
   - If such `i` exists, find index `j` (from the end) such that `nums[j] > nums[i]`.  
   - Swap `nums[i]` and `nums[j]`.  

3. **Reverse the suffix** (right part of the array after index `i`):  
   - Reverse the elements from index `i+1` to the end of the array.  
   - This ensures the suffix is arranged in the smallest lexicographical order.  

⚡ **Time Complexity:** `O(n)`  
⚡ **Space Complexity:** `O(1)` (in-place)
