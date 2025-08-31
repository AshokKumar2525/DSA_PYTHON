from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        B = max(nums).bit_length()  
        LIMIT = 1 << B

        best = [-1] * LIMIT
        for num in nums:
            best[num] = max(best[num], num)

        for b in range(B):
            step = 1 << b
            for mask in range(LIMIT):
                if mask & step:
                    if best[mask ^ step] > best[mask]:
                        best[mask] = best[mask ^ step]

        full_mask = LIMIT - 1
        ans = 0
        for num in nums:
            partner = best[full_mask ^ num]
            if partner != -1:
                ans = max(ans, num * partner)

        return ans
