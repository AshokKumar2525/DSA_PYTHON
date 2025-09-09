# 📢 Number of People Aware of a Secret  

## 📌 Problem Statement  
On **day 1**, one person discovers a secret.  

- Each person will **start sharing** the secret with exactly one new person per day, beginning **`delay` days** after discovering it.  
- Each person will **forget** the secret exactly **`forget` days** after discovering it.  
- Once forgotten, they cannot share anymore.  

Given an integer `n`, return the number of people who still **remember the secret** at the **end of day n**.  
Since the answer may be very large, return it **modulo 10^9 + 7**.  

---

## 🔍 Examples  

### ✅ Example 1  
**Input:**  
```
n = 6, delay = 2, forget = 4
```
**Output:**  
```
5
```

**Explanation:**  
- **Day 1:** Person A learns the secret → (1 person)  
- **Day 2:** Only A knows → (1 person)  
- **Day 3:** A shares with B → (2 people)  
- **Day 4:** A shares with C → (3 people)  
- **Day 5:** A forgets, B shares with D → (3 people)  
- **Day 6:** B shares with E, C shares with F → (5 people)  

---

### ✅ Example 2  
**Input:**
```  
n = 4, delay = 1, forget = 3
```
**Output:**  
```
6
```

**Explanation:**  
- **Day 1:** A learns → (1 person)  
- **Day 2:** A shares with B → (2 people)  
- **Day 3:** A & B share with C and D → (4 people)  
- **Day 4:** A forgets, B, C, D share with 3 new people → (6 people)  

---

## ⚙️ Constraints  
- `2 <= n <= 1000`  
- `1 <= delay < forget <= n`  

---

## 🧠 Approach  

We use **Dynamic Programming (DP)**:  

1. Let `dp[i]` = number of people who **first learn the secret on day i**.  
   - `dp[1] = 1` (only one person on day 1).  

2. Maintain a rolling variable `shareable` = number of people currently eligible to share.  

   - On day `d`:  
     - People who learned on day `d - delay` **start sharing today**.  
     - People who learned on day `d - forget` **forget today**, so they stop contributing.  

3. Each day `d`, the number of new learners = `shareable`.  
   - Hence, `dp[d] = shareable`.  

4. Final answer = sum of people who **still remember at day n**, i.e. those who learned in `[n - forget + 1, n]`.  

---

## ⏱️ Complexity Analysis  
- **Time Complexity:** `O(n)`  
  - We simulate each day once.  
- **Space Complexity:** `O(n)`  
  - DP array stores number of new learners per day.  
