import heapq
from typing import List
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def gain(passed, total):
            return (passed + 1) / (total + 1) - passed / total

        max_heap = []
        sum_pass = 0.0

        for pass_, total in classes:
            sum_pass += pass_ / total
            heapq.heappush(max_heap, (-gain(pass_, total), pass_, total))

        for _ in range(extraStudents):
            current_gain, pass_, total = heapq.heappop(max_heap)
            sum_pass -= pass_ / total
            pass_ += 1
            total += 1
            sum_pass += pass_ / total
            heapq.heappush(max_heap, (-gain(pass_, total), pass_, total))

        return sum_pass / len(classes)