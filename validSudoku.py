class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                # Check column
                if board[r][c] != '.':
                    if board[r][c] in cols[c]:
                        return False
                    else:
                        cols[c].add(board[r][c])

                    # Check row
                    if board[r][c] in rows[r]:
                        return False
                    else:
                        rows[r].add(board[r][c])

                    # Check square
                    square = (r // 3) * 3 + (c // 3)
                    if board[r][c] in squares[square]:
                        return False
                    else:
                        squares[square].add(board[r][c])
        
        return True