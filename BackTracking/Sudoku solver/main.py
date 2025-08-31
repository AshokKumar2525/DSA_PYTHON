class Solution:
    def solveSudoku(self, board):
        # Helper: Returns the box index (0~8) for position (i, j)
        def box_index(i, j):
            return (i // 3) * 3 + (j // 3)

        # Prepare flags for numbers already used
        row_used = [[False]*10 for _ in range(9)]
        col_used = [[False]*10 for _ in range(9)]
        box_used = [[False]*10 for _ in range(9)]
        blanks = []

        # Initialize used flags and blanks list
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    blanks.append((i, j))
                else:
                    num = int(board[i][j])
                    row_used[i][num] = True
                    col_used[j][num] = True
                    box_used[box_index(i, j)][num] = True

        def backtrack(pos):
            if pos == len(blanks):
                return True
            i, j = blanks[pos]
            b = box_index(i, j)
            for num in range(1, 10):
                if not row_used[i][num] and not col_used[j][num] and not box_used[b][num]:
                    # Place number
                    board[i][j] = str(num)
                    row_used[i][num] = col_used[j][num] = box_used[b][num] = True
                    if backtrack(pos + 1):
                        return True
                    # Undo
                    board[i][j] = '.'
                    row_used[i][num] = col_used[j][num] = box_used[b][num] = False
            return False

        backtrack(0)
