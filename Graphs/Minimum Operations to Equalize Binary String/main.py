from collections import deque
from sortedcontainers import SortedList  # pip install sortedcontainers

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        a0 = s.count('0')
        if a0 == 0:
            return 0  

        INF = -1
        dist = [INF] * (n + 1)
        dist[a0] = 0

        even = SortedList(range(0, n + 1, 2))
        odd  = SortedList(range(1, n + 1, 2))

        # remove starting point
        (even if a0 % 2 == 0 else odd).discard(a0)

        q = deque([a0])

        while q:
            a = q.popleft()
            steps = dist[a]
            b = n - a
            x_lo = max(0, k - b)
            x_hi = min(k, a)
            if x_lo > x_hi:
                continue  

            L = a + k - 2 * x_hi
            R = a + k - 2 * x_lo
            L = max(0, L)
            R = min(n, R)
            if L > R:
                continue

            bucket = even if ((a + k) & 1) == 0 else odd
            i = bucket.bisect_left(L)
            to_take = []
            while i < len(bucket):
                v = bucket[i]
                if v > R:
                    break
                to_take.append(v)
                i += 1

            for v in to_take:
                bucket.remove(v)  
                if dist[v] == INF:
                    dist[v] = steps + 1
                    if v == 0:
                        return dist[v]  
                    q.append(v)

        return -1  
