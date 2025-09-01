# [1792. Maximum Average Pass Ratio](https://leetcode.com/problems/maximum-average-pass-ratio/description/?envType=daily-question&envId=2025-09-01)

## 📌 Problem Statement

There is a school that has multiple classes of students, and each class will be having a final exam.  

- You are given a 2D integer array `classes`, where `classes[i] = [passᵢ, totalᵢ]`.  
- In the `iᵗʰ` class, there are `totalᵢ` students, but only `passᵢ` will pass the exam.  
- You are also given an integer `extraStudents`. These students are **guaranteed** to pass any class they are assigned to.  

👉 Goal: Assign each of the `extraStudents` to some class to **maximize** the **average pass ratio** across all classes.  

- **Pass ratio of a class** = `passᵢ / totalᵢ`.  
- **Average pass ratio** = `(sum of pass ratios of all classes) / (number of classes)`.  

Return the **maximum possible average pass ratio** after assigning the extra students.  
Answers within `10^-5` of the actual answer will be accepted.

---

## 🔹 Example 1
**Input:**
```text
classes = [[1,2],[3,5],[2,2]], extraStudents = 2
```
**Output:**  
```text
0.78333
```
**Explanation:**  
- Best assignment: add one student to class `[1,2] → [2,3]`, and one to `[3,5] → [4,6]`.  
- Ratios = `[2/3, 4/6, 2/2] = [0.666, 0.666, 1.0]`  
- Average = `(0.666 + 0.666 + 1.0) / 3 = 0.7833`  

---

### ✅ Example 2  
**Input:**  
```
classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
```
**Output:**  
```
0.53485
```

---

## ⚙️ Constraints  
- `1 <= classes.length <= 10^5`  
- `1 <= passi <= totali <= 10^5`  
- `1 <= extraStudents <= 10^5`  

---

## 🧠 Approach  

We want to **greedily assign each extra student** to the class where they improve the pass ratio the most.  

### 🔑 Key Ideas:  
1. For each class `(p, t)`, the **current ratio** is `p / t`.  
2. If we add one student:  
   - New ratio = `(p+1) / (t+1)`  
   - **Gain = (p+1)/(t+1) - p/t**  
3. Always assign the student to the class with the **maximum gain**.  
4. Use a **max heap (priority queue)** to efficiently track the class with the highest gain.  
5. Repeat until all `extraStudents` are assigned.  

---

## ⏱️ Complexity Analysis  
- **Time Complexity:** `O((n + extraStudents) log n)`  
  - Each heap operation is `O(log n)`.  
- **Space Complexity:** `O(n)`  
  - For storing all classes in the heap.  

---
