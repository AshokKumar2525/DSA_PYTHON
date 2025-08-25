class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat: return []

        m, n = len(mat), len(mat[0])
        res = []

        for d in range(m + n - 1):
            if d < m:
                r, c = d, 0
            else:
                r, c = m - 1, d - m + 1

            diagonal = []
            while r >= 0 and c < n:
                diagonal.append(mat[r][c])
                r -= 1
                c += 1

            if d % 2:
                res.extend(diagonal[::-1])
            else:
                res.extend(diagonal)
        return res
