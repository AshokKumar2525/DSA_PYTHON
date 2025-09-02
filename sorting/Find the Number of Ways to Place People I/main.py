from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ways = 0

        # Sort by x ascending, y descending
        points.sort(key=lambda p: (p[0], -p[1]))

        for i in range(n):
            x1, y1 = points[i]
            candidate_y = -1  # lowest y seen so far (blocker)

            for j in range(i + 1, n):
                x2, y2 = points[j]
                if y2 <= y1:
                    if y2 > candidate_y:
                        # First reachable point without blockers
                        ways += 1
                        candidate_y = y2

        return ways
