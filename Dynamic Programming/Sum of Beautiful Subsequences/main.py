from typing import List

class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        if n == 0:
            return 0

        maxA = max(nums)

        uniq_vals = list(set(nums))
        divs_map = {}
        for v in uniq_vals:
            dv = []
            r = int(v**0.5)
            for d in range(1, r + 1):
                if v % d == 0:
                    dv.append(d)
                    other = v // d
                    if other != d:
                        dv.append(other)
            divs_map[v] = dv

        L = [[] for _ in range(maxA + 1)]
        for v in nums:                    
            for d in divs_map[v]:
                L[d].append(v // d)

        mu = [0] * (maxA + 1)
        mu[1] = 1
        is_comp = [False] * (maxA + 1)
        primes = []
        for i in range(2, maxA + 1):
            if not is_comp[i]:
                primes.append(i)
                mu[i] = -1
            for p in primes:
                ip = i * p
                if ip > maxA:
                    break
                is_comp[ip] = True
                if i % p == 0:
                    mu[ip] = 0
                    break
                else:
                    mu[ip] = -mu[i]

        A = [0] * (maxA + 1)

        for d in range(1, maxA + 1):
            arr = L[d]
            if not arr:
                continue

            vals = sorted(set(arr))
            idx_map = {v: i+1 for i, v in enumerate(vals)}
            m = len(vals)

            bit = [0] * (m + 1)

            def bit_add(i, val):
                while i <= m:
                    bit[i] += val
                    if bit[i] >= MOD:
                        bit[i] -= MOD
                    i += i & -i

            def bit_sum(i):
                s = 0
                while i > 0:
                    s += bit[i]
                    if s >= MOD:
                        s -= MOD
                    i -= i & -i
                return s

            total = 0
            for x in arr:
                idx = idx_map[x]
                s = bit_sum(idx - 1)          
                dp = s + 1                     
                if dp >= MOD:
                    dp -= MOD
                bit_add(idx, dp)
                total += dp
                if total >= MOD:
                    total -= MOD

            A[d] = total

        ans = 0
        for g in range(1, maxA + 1):
            s = 0
            mg = g
            t = 1
            while mg <= maxA:
                mt = mu[t]
                if mt != 0:
                    s += mt * A[mg]
                t += 1
                mg += g
            s %= MOD
            if s < 0:
                s += MOD
            ans = (ans + (g % MOD) * s) % MOD

        return ans
