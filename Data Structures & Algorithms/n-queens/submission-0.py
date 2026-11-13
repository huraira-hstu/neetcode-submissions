class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        colUsed = [False] * n
        leftDiag = [False] * (2 * n -1)
        rightDiag = [False] * (2 * n -1)

        board = [['.'] * n for _ in range(n)]

        def place(i: int, j: int) -> None:
            board[i][j] = 'Q'
            colUsed[j] = True
            leftDiag[j-i+n-1] = True
            rightDiag[j+i] = True
        
        def remove(i: int, j: int) -> None:
            board[i][j] = '.'
            colUsed[j] = False
            leftDiag[j-i+n-1] = False
            rightDiag[j+i] = False

        def safe(i:int, j: int) -> bool:
            return (
                not colUsed[j] and 
                not leftDiag[j - i + n - 1] and 
                not rightDiag[i + j]
            )
        
                
        def backtrack(i: int) -> None:
            if i == n:
                res.append(["".join(row) for row in board])
                return

            for j in range(n):
                if safe(i, j):
                    place(i, j)
                    backtrack(i + 1)
                    remove(i, j)

        backtrack(0)

        return res
        