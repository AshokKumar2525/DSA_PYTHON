class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber -= 1  # adjust for 1-indexed
            res = chr(65 + (columnNumber % 26)) + res
            columnNumber //= 26
        return res
