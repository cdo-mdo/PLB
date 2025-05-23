class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return 

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return

            board[r][c]= '#'  # mark as visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Mark border-connected 'O's
        for r in range(rows):
            if (board[r][0] == 'O'):
                dfs(r, 0)
            if (board[r][cols - 1] == 'O'):
                dfs(r, cols - 1)
        for c in range(cols):
            if (board[0][c] == 'O'):
                dfs(0, c)
            if (board[rows - 1][c] == 'O'):
                dfs(rows - 1, c)

        # Step 2: Flip surrounded 'O' to 'X', revert '#' to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'

