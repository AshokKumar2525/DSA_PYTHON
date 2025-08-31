from typing import List

class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        tmp = n
        primes = []
        d = 2
        while d * d <= tmp:
            while tmp % d == 0:
                primes.append(d)
                tmp //= d
            d += 1
        if tmp > 1:
            primes.append(tmp)

        primes.sort(reverse=True)
        m = len(primes)

        rem_prod = [1] * (m + 1)
        for i in range(m - 1, -1, -1):
            rem_prod[i] = rem_prod[i + 1] * primes[i]

        groups = [1] * k
        best_diff = float('inf')
        best_split = None
        seen = set()

        def dfs(i: int):
            nonlocal best_diff, best_split

            if i == m:
                diff = max(groups) - min(groups)
                if diff < best_diff:
                    best_diff = diff
                    best_split = groups.copy()
                return

            state = (i, tuple(sorted(groups)))
            if state in seen:
                return
            seen.add(state)

            current_max = max(groups)
            current_min = min(groups)
            optimistic_min = current_min * rem_prod[i]
            best_possible_final_diff = current_max - optimistic_min

            if best_possible_final_diff >= best_diff:
                return

            p = primes[i]
            used = set()
            for j in range(k):
                if groups[j] in used:
                    continue
                used.add(groups[j])

                groups[j] *= p
                dfs(i + 1)
                groups[j] //= p

                if groups[j] == 1:
                    break

        dfs(0)

        if best_split is None:
            return sorted(groups)
        return sorted(best_split)
