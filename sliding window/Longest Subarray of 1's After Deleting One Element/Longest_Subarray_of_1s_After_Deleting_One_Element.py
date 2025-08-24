class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros, max_ones = 0, 0
        l = r = 0

        while r < len(nums):
            if nums[r] == 1:
                r += 1
            elif zeros < 1:
                r += 1
                zeros += 1
            else:
                max_ones = max(max_ones, r - l - 1)
                while zeros == 1:
                    if nums[l] == 0:
                        zeros -= 1
                    l += 1
                r += 1
                zeros += 1

        return max(max_ones, r - l - 1)
