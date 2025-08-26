class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Helper: Calculate days needed for given capacity
        def days_needed(cap: int) -> int:
            d = 1
            load = 0
            for w in weights:
                if load + w > cap:
                    d += 1
                    load = 0
                load += w
                if d > days:
                    return d  # Early stop if exceeding days
            return d

        # Binary search boundaries
        low = max(weights)         # At least max package
        high = sum(weights)        # At most sum of all packages

        # Binary search for minimum capacity
        while low <= high:
            mid = (low + high) // 2
            need = days_needed(mid)
            if need <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low
