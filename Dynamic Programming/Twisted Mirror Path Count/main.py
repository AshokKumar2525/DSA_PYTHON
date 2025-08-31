from typing import List
from functools import lru_cache

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dp(r, c, dir):
            if r >= m or c >= n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1

            if grid[r][c] == 1:  # Mirror cell
                if dir == 0:   # came from top → must go right
                    return dp(r, c + 1, 1) % MOD
                else:          # came from left → must go down
                    return dp(r + 1, c, 0) % MOD
            else:  # Empty cell → free move
                return (dp(r + 1, c, 0) + dp(r, c + 1, 1)) % MOD

        # Start either going down or right from (0, 0)
        return (dp(1, 0, 0) + dp(0, 1, 1)) % MOD
