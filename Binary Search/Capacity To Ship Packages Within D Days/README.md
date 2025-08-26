# [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/)

A conveyor belt has packages that must be shipped from one port to another within `days` days.  

The `i^th` package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship.  

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

---

## Example 1
```
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of
capacity 14 and splitting the packages differently is not allowed.
```

---

## Example 2

```
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
```

---

## Example 3

```
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
```

---

## Constraints

- `1 <= days <= weights.length <= 5 * 10^4`
- `1 <= weights[i] <= 500`

---

## Approach 🚀

We need to find the **minimum ship capacity** that allows us to deliver all packages within the given `days`.  
This is a **binary search on the answer** problem.  

### Step-by-step approach:
1. **Define the search space**:  
   - Minimum possible capacity = `max(weights)` (since at least one day will carry the heaviest package).  
   - Maximum possible capacity = `sum(weights)` (if we ship all packages in 1 day).  

2. **Check feasibility with a helper function**:  
   - Write a function `days_needed(cap)` that returns how many days are required if the ship capacity is `cap`.  
   - Iterate through weights sequentially, and whenever the current load exceeds `cap`, start a new day.
   - If the needy days greater than days , stop early to make sure not to loop unnecessary iterations   

3. **Binary search**:  
   - If `days_needed(mid)` ≤ `days`, then `mid` is a valid capacity, but we try smaller (move left).  
   - Else, we need a bigger capacity (move right).  

4. **Final answer**:  
   - When binary search finishes, `low` will be the minimum capacity needed.  

---
